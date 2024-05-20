"""
do spotify requests

need requests library using 
pip install requests
"""
import requests

from os.path import realpath, dirname
import json

DIR = dirname(realpath(__file__))

# TODO: fill in CLIENT_ID and CLIENT_SECRET
CLIENT_ID = 'PASTE_YOUR_CLIENT_ID_HERE'
CLIENT_SECRET = 'PASTE_YOUR_CLIENT_SECRET_HERE'

# LOGIN USING CLIENT ID AND CLIENT SECRET

AUTH_URL = 'https://accounts.spotify.com/api/token'
LOGIN_DICT = {
    'grant_type':'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
  }
AUTH_TOKEN_KEY = 'access_token'
auth_resp = requests.post( AUTH_URL, LOGIN_DICT )
auth_resp_data = auth_resp.json()
access_token = auth_resp_data[AUTH_TOKEN_KEY]

HEADERS = {
        'Authorization': f'Bearer {access_token}',
    }

# get the play list by playlist id

my_playlist = [ ]

PLAYLIST_ID = '17Boxd497nci9642xPt1HB'
url = f'https://api.spotify.com/v1/playlists/{PLAYLIST_ID}/tracks?offset=0&limit=100'

while (url is not None):
  resp = requests.get(url,
    headers=HEADERS
    )

  # only continue is resp is ok
  if not resp.ok :
    print( f'status: {resp.status_code}')
    exit()

  # load the "json" data
  spotify_data = json.loads( resp.text )

  # extract info and put into my playlist
  for row in spotify_data['items']:
    track = row['track']
    track_name = track['name']
    track_id = track['id']
    artists = track['artists']
    artist  = None
    if len( artists ) == 1 :
      artist_id = artists[ 0 ]['id']
      artist_name = artists[ 0 ]['name']
    else:
      artist_id = -1
      artist_name = 'many'
    
    my_playlist.append(  { 'id' : track_id, 
                          'name': track_name, 
                          'artist_id': artist_id, 
                          'artist_name':artist_name } )

  # next 100 tracks
  url = spotify_data['next']

# output the results
for i,track in enumerate(my_playlist):
  print( f'{i},{track["id"]},{track["name"]},' \
        f'{track["artist_id"]},{track["artist_name"]}' )

