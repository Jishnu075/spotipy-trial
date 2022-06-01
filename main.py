# GET https://api.spotify.com/v1/search
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

# change scope accordingly
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET,
                                               redirect_uri=cred.redirect_url, scope=scope))


# results = sp.search(type="playlist", q="sad", limit=1, market="US")
# x = results["playlists"]["items"][0]["external_urls"]['spotify']
# print(x)

def getplaylist(mood):
    results = sp.search(type="playlist", q=mood, limit=1, market="US")
    x = results["playlists"]["items"][0]["external_urls"]['spotify']
    return x
mood = "surprise"
print(getplaylist(mood=mood))

# results = sp.category_playlists(category_id="")
# results = sp.recommendations(seed_genres="happy")
