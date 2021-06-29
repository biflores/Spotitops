# Shows the top tracks for a user

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=config('SPOTIPY_CLIENT_ID'),
    client_secret=config('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=config('SPOTIPY_REDIRECT_URL'),
    scope=scope))

ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()
