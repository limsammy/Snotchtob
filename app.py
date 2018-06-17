
import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

import json
from IPython import embed
from pytube import YouTube
import unicodedata

CLIENT_SECRETS_FILE = "client_secrets.json"
DEVELOPER_KEY = "AIzaSyCZDE98UD5cUa15DJquhW5Jc9bxusijWcc"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  # flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  # credentials = flow.run_console()
  # return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
  return build(API_SERVICE_NAME, API_VERSION,
    developerKey=DEVELOPER_KEY)


def print_response(response):
  print(response)

def build_resource(properties):
  resource = {}
  import code; code.interact(local=dict(globals(), **locals()))
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]

      # For properties that have array values, convert a name like
      # "snippet.tags[]" to snippet.tags, and set a flag to handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True

      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

def remove_empty_kwargs(**kwargs):
  good_kwargs = {}
  if kwargs is not None:
    for key, value in kwargs.iteritems():
      if value:
        good_kwargs[key] = value
  return good_kwargs

def playlist_items_list_by_playlist_id(client, **kwargs):
  kwargs = remove_empty_kwargs(**kwargs)

  response = client.playlistItems().list(
    **kwargs
  ).execute()
  response = json.dumps(response)
  json_response = json.loads(response)
  
  data = sanitize_data(json_response['items'])

  create_directory()

  download_videos(data)
  # return print_response(response)

def sanitize_data(playlist):
  videos = []
  for video in playlist:
    resource = {}
    id = unicodedata.normalize('NFKD', video['snippet']['resourceId']['videoId']).encode('ascii','ignore')
    title = unicodedata.normalize('NFKD', video['snippet']['title']).encode('ascii','ignore')

    resource['id'] = id
    resource['title'] = title

    videos.append(resource)
  return videos

def download_videos(videos_list):
  for video in videos_list:
    link = "http://youtube.com/watch?v={}".format(video['id'])
    YouTube(link).streams.first().download('./videos')
    print("Downloaded {}").format(video['title'])

def create_directory():
  if not os.path.exists('./videos'):
    os.makedirs('./videos')

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  client = get_authenticated_service()
  
  playlist_items_list_by_playlist_id(client,
    part='snippet,contentDetails',
    maxResults=25,
    playlistId='PLcKFH-qaX7yigdFDf6WplLkFaMLSp9jeH')
