# All Controllers of the MVC Architecture go here.
from PySide import QtCore, QtGui
import views

class MainWindowController(QtGui.QMainWindow, views.MainWindowView):

    def __init__(self):
       super(MainWindowController, self).__init__()
       self.setupUi(self)
       self.setCentralWidget(TrackDownloaderController())
       self.show()


class TrackDownloaderController(QtGui.QWidget, views.TrackDownloaderView):

    def __init__(self):
        super(TrackDownloaderController, self).__init__()
        self.setupUi(self)