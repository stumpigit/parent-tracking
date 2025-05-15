import { SvelteKitAuth } from '@auth/sveltekit';
import keycloak from '@auth/sveltekit/providers/keycloak';


import { env } from '$env/dynamic/private';


export const { handle, signIn, signOut } = SvelteKitAuth(async () => {
	const authOptions = {
		providers: [
			keycloak({
				clientId: env.AUTH_KEYCLOAK_ID,
				clientSecret: env.AUTH_KEYCLOAK_SECRET,
				issuer: env.AUTH_KEYCLOAK_ISSUER
			})
		],
		secret: env.AUTH_SECRET,
		trustHost: true,
		debug: true,
		callbacks: {
			async jwt({ token, account }) {
				if (account) {
					return { ...token, accessToken: account.access_token }
				}
				return token
			},
			async session({ session, token }) {
				session.accessToken = token.accessToken
				return session
			}
		}
	};
	return authOptions;
});
