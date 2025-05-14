from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.responses import FileResponse

from .AirTagCrypto import AirTagCrypto
import requests
from datetime import datetime

router = APIRouter(prefix="/tracker",
    tags=["tracker"],)

@router.get("/{tracker_id}")
def get_tracker(tracker_id):
    key = "B/osdwWlX/SEqt9Zqzqb92QOt+U6tjPkRGE8fw=="

    tags = {}
    tag = AirTagCrypto(key)
    tags[tag.get_advertisement_key()] = tag

    data = requests.post("https://tracking.suter-burri.ch", json={"ids": list(tags.keys()), "days": 2}).json()

    entries = []
    for result in data['results']:
            decrypt = tags[result['id']].decrypt_message(result['payload'])
            date_time = datetime.fromtimestamp(decrypt['timestamp'])
            entry = {'date': date_time.strftime("%d.%m.%Y %H:%M:%S"),
                        'lat': decrypt['lat'],
                        'lon': decrypt['lon']}
            entries.append(entry)
    return entries

