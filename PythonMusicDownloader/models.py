# All models of the MVC architecture go here.
import requests
import json

class TrackDownloader(object):
    """Downloads songs from pleer.com"""
    def __init__(self, id, key, query=None, download_dir=None):
        """
        :param id: Id of Pleer API access.
        :type id: int
        :param key: key of Pleer API Access.
        :type key: str
        :param query: Query of user.
        :type query: str
        :param download_dir: Download directory.
        :type download_dir: str
        """
        self.API_TOKEN_URL = "http://api.pleer.com/token.php"
        self.API_URL = "http://api.pleer.com/index.php"
        self.id = id
        self.key = key
        self.query = query
        self.download_dir = download_dir
        self.token = self.get_access_token()
        self.tracks = []

    def get_access_token(self):
        """Get access token from pleer.com"""
        auth = (self.id, self.key)
        data = {"grant_type": "client_credentials"}
        response = requests.post(self.API_TOKEN_URL, auth=auth, data=data)
        token = response.json().get("access_token")
        return token

    def tracks_search(self, query, page=1, result_on_page=10, quality="all"):
        """Search for tracks
        :param query: Query of user.
        :type query: str
        :param page: Selected page.
        :type page: int
        :param result_on_page: Amount of results on a page.
        :type result_on_page: int
        :param quality: Quality of file desired.
        :type quality: str
        """
        data = {
            'access_token': self.token,
            'query': query,
            'page': page,
            'result_on_page': result_on_page,
            'quality': quality    
        }
        response = requests.post(self.API_TOKEN_URL, data=data)
        tracks = response.json().get("tracks")
        for track in tracks:
            tracks.append(Track(track))


class Track(object):
    """Holds data of a track"""
    def __init__(self, track):
        """
        :param track: Metadata of track.
        :type track: list.
        """
        self.id = track['track_id']
        self.artist = track['artist']
        self.track = track['track']
        self.length = track['length']
        self.bitrate = track['bitrate']
        self.size = track['size']

