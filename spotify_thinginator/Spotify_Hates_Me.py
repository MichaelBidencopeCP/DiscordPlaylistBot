
import spotipy
from spotipy import oauth2
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials



SPOTIPY_CLIENT_ID = '6d1d5e7db377484d9ee572da4f0c3363'
SPOTIPY_CLIENT_SECRET = 'f3d1c1dc8e6f4894ac8649357e74c17c'
SPOTIPY_REDIRECT_URI = 'https://localhost:8888/callback'
SPOTIPY_PLAYLIST_ID = '3kKtMS3Qjt2ZTC4G70WxJc'

SCOPE = "user-library-read"
CACHE = '.cache/spotipyocache'

#sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE,cache_path=CACHE))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
