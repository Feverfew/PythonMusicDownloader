# All Controllers of the MVC Architecture go here.
from PySide import QtCore, QtGui
import views
import models

class MainWindowController(QtGui.QMainWindow, views.MainWindowView):
    """Controller for the main window of the application"""
    def __init__(self):
       super(MainWindowController, self).__init__()
       self.setupUi(self)
       self.setCentralWidget(TrackDownloaderController())
       self.show()


class TrackDownloaderController(QtGui.QWidget, views.TrackDownloaderView):
    """Controller for the track downloader widget"""
    def __init__(self):
        super(TrackDownloaderController, self).__init__()
        self.setupUi(self)
        # Make Table contents fit size of window.
        self.results_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.trackdownloader = models.TrackDownloader("313666", "Eb0iVMUcPeym8f8JEKWG")
        self.trackdownloader.get_top_list()
        self.show_track_data()

    def show_track_data(self):
        """Get tracks from TrackDownloader and display on QTableWidget"""
        self.results_table.clearContents()
        i = 0
        for track in self.trackdownloader.tracks:
            artist = QtGui.QTableWidgetItem()
            artist.setText(track.artist)
            title = QtGui.QTableWidgetItem()
            title.setText(track.track)
            length = QtGui.QTableWidgetItem()
            length.setText(track.length)
            bitrate = QtGui.QTableWidgetItem()
            bitrate.setText(track.bitrate)
            self.results_table.insertRow(i)
            self.results_table.setItem(i, 0, artist)
            self.results_table.setItem(i, 1, title)
            self.results_table.setItem(i, 2, length)
            self.results_table.setItem(i, 3, bitrate)
