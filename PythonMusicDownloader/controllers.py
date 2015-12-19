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
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.actionAbout_Author.activated.connect(self.open_author_page)
        self.actionAbout_Program.activated.connect(self.open_project_page)
        self.actionReport_a_Bug.activated.connect(self.open_issue_page)
        self.show()

    def open_author_page(self):
        """Opens the author's page in the user's browser"""
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/Feverfew"))

    def open_project_page(self):
        """Opens the program's page in the user's browser"""
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/Feverfew/PythonMusicDownloader"))

    def open_issue_page(self):
        """Opens the issues page in the user's browser"""
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/Feverfew/PythonMusicDownloader/issues"))


class TrackDownloaderController(QtGui.QWidget, views.TrackDownloaderView):
    """Controller for the track downloader widget"""
    def __init__(self):
        super(TrackDownloaderController, self).__init__()
        self.setupUi(self)
        # Make Table contents fit size of window.
        self.results_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        # Selecting cell selects whole row
        self.results_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.results_table.hideColumn(4)
        self.results_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        self.trackdownloader = models.TrackDownloader("313666", "Eb0iVMUcPeym8f8JEKWG")

        self.threads = []

        # Event Handlers
        self.search_btn.clicked.connect(self.search_tracks)
        self.next_page_btn.clicked.connect(self.next_page)
        self.prev_page_btn.clicked.connect(self.previous_page)
        self.skip_to_btn.clicked.connect(self.skip_to_page)
        self.download_dir_btn.clicked.connect(self.find_download_dir)
        self.download_btn.clicked.connect(self.download_tracks)
        #self.artist_field.keyPressEvent(self.update_artist_suggestions())
        #self.track_field.keyPressEvent(self.update_track_suggestions())

        #Autocomplete
        #self.artist_completer = QtGui.QCompleter()
        #self.artist_field.setCompleter(self.artist_completer)
        #self.track_completer = QtGui.QCompleter()
        #self.track_field.setCompleter(self.track_completer)
        #self.track_suggestions = QtGui.QStringListModel()
        #self.artist_suggestions = QtGui.QStringListModel()
        #self.artist_completer.setModel(self.trackdownloader.suggestions)
        #self.track_completer.setModel(self.trackdownloader.suggestions)


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
            identifier = QtGui.QTableWidgetItem()
            identifier.setText(track.id)
            self.results_table.insertRow(i)
            self.results_table.setItem(i, 0, artist)
            self.results_table.setItem(i, 1, title)
            self.results_table.setItem(i, 2, length)
            self.results_table.setItem(i, 3, bitrate)
            self.results_table.setItem(i, 4, identifier)
            i += 1
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
        msg_box = QtGui.QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setWindowIcon(QtGui.QIcon("icon.ico"))
        msg_box.setText(error)
        msg_box.exec_()

    def find_download_dir(self):
        """Let the user choose his desired download directory."""
        self.trackdownloader.download_dir = QtGui.QFileDialog().getExistingDirectory()
        self.download_dir_field.setText(self.trackdownloader.download_dir)

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
            # TODO Add exception.
            try:
                self.trackdownloader.page = int(float(self.skip_to_field.text()))
            except ValueError:
                self.trackdownloader.page = 1
            self.search_tracks()

    def is_new_search(self):
        """Found out if it is a new search or if just going to different page of results."""
        artist_query = self.artist_field.text()
        track_query = self.track_field.text()
        if artist_query != "" and track_query != "":
            if self.trackdownloader.query == "artist:{} track:{}".format(artist_query, track_query):
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


    def update_track_suggestions(self):
        # TODO Artist field autocomplete.
        pass

    def update_artist_suggestions(self):
        # TODO Artist field autocomplete.
        pass

    def download_tracks(self):
        """Downloads the selected track."""
        if self.download_dir_field.text() != "":
            row = self.results_table.currentRow()
            if row != -1:
                identifier = self.results_table.item(row, 4).text()
                artist = self.results_table.item(row, 0).text()
                track = self.results_table.item(row, 1).text()
                self.threads.append(DownloadThread(self.trackdownloader, identifier, artist, track))
                self.threads[-1].start()
            else:
                self.trackdownloader.errors = "Error: Please select a song to download."
                self.show_errors()
        else:
            self.trackdownloader.errors = "Error: Please select a download directory."
            self.show_errors()

class DownloadThread(QtCore.QThread):
    """Thread for downloading mp3 file."""
    def __init__(self, trackdownloader, identifier=None, artist=None, track=None, parent=None):
        super(DownloadThread, self).__init__(parent)
        self.trackdownloader = trackdownloader
        self.identifier = identifier
        self.artist = artist
        self.track = track

    def run(self):
        """Starting this thread downloads the track"""
        self.trackdownloader.download_track(self.identifier, self.artist, self.track)
