import unittest
from models import SongDownloader

class SongDownloaderTestCase(unittest.TestCase):

    def test_attributes_are_set_when_object_initialised(self):
        test_data = [["Opeth", "Blackwater Park", "C:/"],
                     ["Mono", "Are you there", "C:/Program Files"],
                     ["Sevendust", "Denial", "C:/"]]
        for data in test_data:
            song_downloader = SongDownloader(data[0], data[1], data[2])
            self.assertEquals(song_downloader.artist, data[0])
            self.assertEquals(song_downloader.song, data[1])
            self.assertEquals(song_downloader.download_dir, data[2])

class SongTestCase(unittest.TestCase):

    def test_attributes_are_set_when_object_initialised(self):
        pass


if __name__ == '__main__':
    unittest.main()
