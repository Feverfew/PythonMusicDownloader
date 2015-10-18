# All models of the MVC architecture go here.
import requests
import json

class SongDownloader(object):
    """Downloads songs from pleer.com"""
    def __init__(self, artist, song, download_dir):
        """
        Args:
            artist (str): Name of artist.
            song (str): Name of song.
            download_dir (str) Name of download_dir. 
                Make sure directory is valid or an Exception
                will occur.
        """
        self.artist = artist
        self.song = song
        self.download_dir = download_dir