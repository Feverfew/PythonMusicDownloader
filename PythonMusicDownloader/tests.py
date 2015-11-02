import unittest
from models import TrackDownloader

class TrackDownloaderTestCase(unittest.TestCase):

    def test_attributes_are_set_when_object_initialised(self):
        test_data = [["313666", "Eb0iVMUcPeym8f8JEKWG", None, None],
                     ["345635", "sdr324RFSDv£$Wr13433", "Opeth", None],
                     ["345632", "sdFW£$FVR£E453fsfsss", "Deftones", "C:/"]
                     ]
        for data in test_data:
            song_downloader = TrackDownloader(data[0], data[1], data[2], data[3])
            self.assertEquals(song_downloader.id, data[0])
            self.assertEquals(song_downloader.key, data[1])
            self.assertEquals(song_downloader.query, data[2])
            self.assertEquals(song_downloader.download_dir, data[3])

    def test_for_access_token(self):
        song_downloader = TrackDownloader("313666", "Eb0iVMUcPeym8f8JEKWG")
        self.assertTrue(song_downloader.token)

    def test_for_failure_if_parameters_missing_in_intialisation(self):
        test_data = [[None, None, None, None],
                     ["2342333", None, "Opeth", None],
                     [None, "scgvcdfv2CSF£$RSC", None, "C:/"]
                     ]
        for data in test_data:
            self.assertRaises(TrackDownloader(data[0], data[1], data[2], data[3]))

class TrackTestCase(unittest.TestCase):

    def test_attributes_are_set_when_object_initialised(self):
        pass


if __name__ == '__main__':
    unittest.main()
