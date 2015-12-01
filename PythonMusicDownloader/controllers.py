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
        self.show_track_data()
        self.search_btn.clicked.connect(self.search_tracks)
        self.next_page_btn.clicked.connect(self.next_page)
        self.prev_page_btn.clicked.connect(self.previous_page)
        self.skip_to_btn.clicked.connect(self.skip_to_page)


    def show_track_data(self):
        """Get tracks from TrackDownloader and display on QTableWidget"""
        # Clear table.
        self.results_table.setRowCount(0)
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
        # Show page of results on line edit.
        self.skip_to_field.setText(str(self.trackdownloader.page))


    def search_tracks(self):
        """Get text from line edit and construct query for TrackDownloader"""
        artist_query = self.artist_field.text()
        track_query = self.track_field.text()
        if self.is_new_search():
            self.trackdownloader.page = 1
        if artist_query != "" and track_query != "":
            self.trackdownloader.query = "artist:{} track:{}".format(artist_query, track_query)
            self.trackdownloader.tracks_search()
            self.show_track_data()
        elif artist_query != "":
            self.trackdownloader.query = "artist:{}".format(artist_query)
            self.trackdownloader.tracks_search()
            self.show_track_data()
        elif track_query != "":
            self.trackdownloader.query = "track:{}".format(track_query)
            self.trackdownloader.tracks_search()
            self.show_track_data()
        else: 
            self.trackdownloader.errors = "Error: please enter a search term."

        if self.trackdownloader.errors:
            self.show_errors()

    def show_errors(self):
        """If there are errors show them in a message box."""
        error = self.trackdownloader.errors
        self.trackdownloader.errors = None
        msgBox = QtGui.QMessageBox()
        msgBox.setWindowTitle("Error")
        msgBox.setText(error)
        msgBox.exec_()

    def next_page(self):
        """Go to next page of search criteria"""
        self.trackdownloader.page += 1
        self.search_tracks()

    def previous_page(self):
        """Go to previous page of search criteria"""
        if self.trackdownloader.page == 1:
            self.trackdownloader.errors = "Error: Cannot go to page 0"
            self.show_errors()
        else:
            self.trackdownloader.page -= 1
            self.search_tracks()

    def skip_to_page(self):
        """Got to page defined in the line edit"""
        if self.skip_to_field.text() == '0':
            self.trackdownloader.errors = "Error: Cannot go to page 0"
            self.show_errors()
        else:
            self.trackdownloader.page = int(self.skip_to_field.text())
            self.search_tracks()

    def is_new_search(self):
        """Found out if it is a new search or if just going to different page of results."""
        artist_query = self.artist_field.text()
        track_query = self.track_field.text()
        if artist_query != "" and track_query != "":
            if self.trackdownloader.query == "artist:{} track:{}".format(artist_query, track_query):#
                return False
            else:
                return True
        elif artist_query != "":
            if self.trackdownloader.query == "artist:{}".format(artist_query):
                return False
            else:
                return True
        elif track_query != "":
            if self.trackdownloader.query == "track:{}".format(track_query):
                return False
            else:
                return True

