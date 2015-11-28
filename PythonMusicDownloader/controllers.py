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