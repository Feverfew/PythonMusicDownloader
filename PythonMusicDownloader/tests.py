import unittest
import models
import controllers
import sys
from PySide import QtGui, QtCore

class TrackDownloaderTestCase(unittest.TestCase):

    def test_for_access_token(self):
        """Test will fail if there is no internet connection"""
        song_downloader = models.TrackDownloader("313666", "Eb0iVMUcPeym8f8JEKWG")
        self.assertTrue(song_downloader.token)

    def test_for_failure_if_parameters_missing_in_intialisation(self):
        test_data = [[None, None, None, None],
                     ["2342333", None, "Opeth", None],
                     [None, "scgvcdfv2CSF£$RSC", None, "C:/"]
                     ]
        for data in test_data:
            self.assertRaises(models.TrackDownloader(data[0], data[1], data[2], data[3]))

class TrackTestCase(unittest.TestCase):
    
    def test_sec_to_min_works(self):
        seconds_data = [60, 120, 3, 63, 100, 95, 600, 599]
        expected_results = ['1m', '2m', '3s', '1m 3s', '1m 40s', '1m 35s', '10m', '9m 59s']
        for i in range(len(seconds_data)):
            self.assertEquals(models.Track.sec_to_min(seconds_data[i]), expected_results[i])
        

if __name__ == '__main__':
    unittest.main()
