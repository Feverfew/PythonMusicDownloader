﻿# All models of the MVC architecture go here.
import requests
import json

class TrackDownloader(object):
    """Downloads songs from pleer.com"""
    def __init__(self, identifier, key, query=None, download_dir=None):
        """
        :param identifier: Id of Pleer API access.
        :type identifier: int
        :param key: key of Pleer API Access.
        :type key: str
        :param query: Query of user.
        :type query: str
        :param download_dir: Download directory.
        :type download_dir: str
        """
        self._API_TOKEN_URL = "http://api.pleer.com/token.php"
        self._API_URL = "http://api.pleer.com/index.php"
        self.identifier = identifier
        self.key = key
        self.query = query
        self.download_dir = download_dir
        self.token = self.get_access_token()
        self.tracks = []
        self.errors = None
        self.page = 1
        self.suggestions = None

    def _get_response(self, **kwargs):
        """Using the token get a response depending no the data given.
        :param kwargs['data']: dictionary of the data.
        :type kwargs['data']: dict
        """
        data = kwargs['data']
        self.errors, response = None, None
        try:
            response = requests.post(self._API_URL, data=data, timeout=10.0)
        except requests.exceptions.ConnectionError:
            self.errors = "Connection error: No connect could be established to server."
        except requests.exceptions.Timeout:
            self.errors = "Connection error: request timedout."
        except ValueError:
            self.errors = "Error: data received is not valid JSON."
        return response


    def get_access_token(self):
        """Get access token from pleer.com"""
        auth = (self.identifier, self.key)
        data = {"grant_type": "client_credentials"}
        token = None
        try:
            response = requests.post(self._API_TOKEN_URL, auth=auth, data=data, timeout=10.0)
            token = response.json().get("access_token")
            return token
        except requests.exceptions.ConnectionError as e:
            self.errors = "Connection error: No connect could be established to server."
        except requests.exceptions.Timeout as e:
            self.errors = "Connection error: request timedout."
        except ValueError:
            self.errors = "Error: data received is not valid JSON."
        return None


    def tracks_search(self, result_on_page=20, quality="all"):
        """Search for tracks
        :param query: Query of user.
        :type query: str
        :param page: Selected page.
        :type page: int
        :param quality: Quality of file desired.
        :type quality: str
        """
        data = {
            'access_token': self.token,
            'method': 'tracks_search',
            'query': self.query,
            'page': self.page,
            'result_on_page': result_on_page,
            'quality': quality
        }
        try:
            response = self._get_response(data=data)
            json_data = json.loads(response.text)
            self.tracks = []
            if json_data['count'] != '0' and json_data ['tracks'] != []:
                for track_id, track_info in json_data['tracks'].items():
                    self.tracks.append(Track(track_info))
            else:
                self.errors = "No tracks were found that met your criteria."
        except AttributeError as e:
            pass


    def tracks_get_info(self, track_id):
        """Gets information and metadata of a track.
        :param track_id: Id of track.
        :type track_id: int
        """
        data = {
            'access_token': self.token,
            'method': 'tracks_get_info',
            'track_id': track_id
        }
        response, track_info = None, None
        try:
            response  = requests.post(self._API_URL, data=data)
        except:
            response = None
        if response:
            track_info = {
                'track_id': track_id,
                'artist': response.json().get('artist'),
                'track': response.json().get('track'),
                'length': response.json().get('length'),
                'bitrate': response.json().get('bitrate'),
                'size': response.json().get('size')
            }
        return track_info
            

    def get_download_url(self, track_id, reason="save"):
        """Gets the download url of a file
        :param track_id: Id of track.
        :type track_id: int
        :param reason: Reason for requesting url.
        :type reason: str
        """
        data = {
            'access_token': self.token,
            'method': 'tracks_get_download_link',
            'track_id': track_id,
            'reason': reason    
        }
        response = requests.post(self._API_URL, data=data)
        json_data = json.loads(response.text)
        return json_data['url']
    
    def get_top_list(self, list_type=1, language="en"):
        """ Gets the most popular songs from pleer.com
        :param list_type: Type of list.
        :type list_type: int
        :param page: Page of results.
        :type page: int
        :param language: Top list from what country (en, ru).
        :type language: str
        """
        data = {
            'access_token': self.token,
            'method': 'get_top_list',
            'list_type': list_type,
            'page': self.page,
            'language': language
        }
        response = self._get_response(data=data)
        json_data = json.loads(response.text)
        self.tracks = []
        for track_id, track_info in json_data['tracks']['data'].items():
            self.tracks.append(Track(track_info))


    def get_suggest(self, part):
        """Gets suggestions based on what user has typed
        :param part: What the user has typed already.
        :type part: str
        """
        data= {
            'access_token': self.token,
            'method': 'get_suggest',
            'part': part
        }
        response = self._get_response(data=data)
        json_data = json.loads(response.text)
        self.suggestions = json_data['suggest']

    def download_track(self, id, artist, track):
        """Downloads a track based on its id
        :param id: id of the track.
        :type id: str
        :param artist: Artist of the track.
        :type artist: str
        :param track: Title of the track.
        :type track: str
        """
        url = self.get_download_url(id)
        if self.download_dir:
            filename = "{}\{} - {}.mp3".format(self.download_dir, artist, track)
            data = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(data.content)
        else:
            self.errors = "Error: Please select a download directory."


class Track(object):
    """Holds data of a track"""
    def __init__(self, track):
        """
        :param track: Metadata of track.
        :type track: dict
        """
        self.id = track['id']
        self.artist = track['artist']
        self.track = track['track']
        # Pleer api spelt length incorrectly...
        self.length = self.sec_to_min(int(track['lenght']))
        self.bitrate = track['bitrate']

    @staticmethod
    def sec_to_min(seconds):
        """Get a value in seconds and convert into minutes.
        :param seconds: Length of song in seconds
        :type seconds: int
        """
        second = seconds % 60
        minutes = int(seconds/60)
        if second == 0:
            return "{}m".format(minutes)
        elif minutes == 0:
            return "{}s".format(second)
        else:
            if second < 10:
                second = "0" + str(second)
            return "{}m {}s".format(minutes, second)

