import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import sys
from datetime import timedelta
from spotipy.oauth2 import SpotifyOAuth

GLOBAL_CLIENT_ID = 'ce6d69e4d2744f39a9ff5c84164b72e5'
GLOBAL_CLIENT_SECRET = '8ddd32222f80488a88cc7819cbcb2fa1'

spotify = None

class SpotifyAPIWrapper:
    def __init__(self):
        authenticator = Authenticator(GLOBAL_CLIENT_ID, GLOBAL_CLIENT_SECRET)
        self.spotify = authenticator.doAuth()

    def getUsersPlaylists(self,username):

        playlists = self.spotify.user_playlists(username)
        playlist_uris = []
        playlist_names = []

        for playlist in playlists['items']:
            print(playlist['name'])
            # playlist_names.append(playlist['name'].encode('ascii','ignore').decode('ascii'))
            # playlist_uris.append(playlists['uri'].split(':')[2])

        
    def getSongsFromPlaylist(self, uri, username, name=""):

        song_list = []
        results = self.spotify.user_playlist(username, uri)
        tracks = results['tracks']

    




class Authenticator:
    def __init__(self, client_id, client_secret):
        self.CLIENT_ID = client_id
        self.CLIENT_SECRET = client_secret
    
    def doAuth(self):
        credentialManager = SpotifyClientCredentials(client_id=self.CLIENT_ID, client_secret=self.CLIENT_SECRET)
        spotify = spotipy.Spotify(client_credentials_manager=credentialManager)
        return spotify
