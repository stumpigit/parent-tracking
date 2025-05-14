import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class AirTagCrypto:
    def __init__(self, private_key: str = None):
        if private_key is not None:
            self._private_key = base64.b64decode(private_key)
        else:
            self._private_key = self.__generate_new_private_key()

	# Get the hashed advertisement key (hash of the public key)
    def get_advertisement_key(self) -> str:
        digest = hashes.Hash(hashes.SHA256())
        digest.update(self.__get_advertisement_key_bytes())
        return base64.b64encode(digest.finalize()).decode()

	# Get the public key
    def get_public_key(self) -> str:
        return base64.b64encode(self.__get_advertisement_key_bytes()).decode("ascii")

	# This function works if you follow the standard of the AirTag, as used in OpenHaystack
    def get_mac_address(self) -> str:
        adv_key = self.__get_advertisement_key_bytes()
        first_hex = adv_key[0] | 0b11000000
        return self.format_byte(first_hex) + ":" + ":".join([self.format_byte(x) for x in adv_key[1:6]])

    @staticmethod
    def format_byte(byte):
        return f'{byte:02x}'.upper()

    # Get the X of the public key in bytes
    def __get_advertisement_key_bytes(self) -> bytes:
        return self.__derive_elliptic_curve_private_key(self._private_key, ec.SECP224R1()).public_key().public_numbers().x.to_bytes(28, 'big')

    @staticmethod
    def __derive_elliptic_curve_private_key(private_key: bytes, curve: ec.EllipticCurve):
        return ec.derive_private_key(int.from_bytes(private_key, 'big'), curve, default_backend())

    def __derive_shared_key_from_private_key_and_eph_key(self, eph_key: bytes):
        curve = ec.SECP224R1()
        private_key = self.__derive_elliptic_curve_private_key(self._private_key, curve)
        public_key = ec.EllipticCurvePublicKey.from_encoded_point(curve, eph_key)
        shared_key = private_key.exchange(ec.ECDH(), public_key)
        return shared_key

    @staticmethod
    def __kdf(shared_key, eph_key: bytes, counter=1):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(shared_key)

        counter_data = bytes(counter.to_bytes(4, 'big'))
        digest.update(counter_data)
        digest.update(eph_key)
        return digest.finalize()

    @staticmethod
    def __decrypt_payload(enc_data: bytes, symmetric_key: bytes, tag: bytes):
        decryption_key = symmetric_key[:16]
        iv = symmetric_key[16:]
        cipher = Cipher(algorithms.AES(decryption_key), modes.GCM(iv, tag))
        decryptor = cipher.decryptor()
        return decryptor.update(enc_data) + decryptor.finalize()

    @staticmethod
    def __decode_tag(data: bytes):
        latitude = int.from_bytes(data[0:4], 'big') / 10000000.0
        longitude = int.from_bytes(data[4:8], 'big') / 10000000.0
        horizontal_acc = int.from_bytes(data[8:9], 'big')
        status = data[9]
        return {'lat': latitude, 'lon': longitude, 'horizontal_acc': horizontal_acc, 'status': status}

    @staticmethod
    def __generate_new_private_key():
        curve = ec.SECP224R1()
        return ec.generate_private_key(curve).private_numbers().private_value.to_bytes(28, 'big')

    def decrypt_message(self, payload):
        data = base64.b64decode(payload)
        if len(data) > 88: data = data[0:4] + data[5:]
        timestamp = int.from_bytes(data[0:4], 'big')
        confidence = data[4]
        eph_key = data[5:62]
        shared_key = self.__derive_shared_key_from_private_key_and_eph_key(eph_key)
        derived_key = self.__kdf(shared_key, eph_key)
        enc_data = data[62:72]
        tag = data[72:]
        decrypted = self.__decrypt_payload(enc_data, derived_key, tag)

        ret = self.__decode_tag(decrypted)
        ret['timestamp'] = timestamp + 978307200  # 978307200 is delta between unix and cocoa timestamps
        ret['confidence'] = confidence
        return ret