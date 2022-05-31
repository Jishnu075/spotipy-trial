# GET https://api.spotify.com/v1/search

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))


# results = sp.category_playlists(category_id="")
# results = sp.recommendations(seed_genres="happy")
results = sp.search(type="playlist", q="sad", limit=5,market="US")
print(results)