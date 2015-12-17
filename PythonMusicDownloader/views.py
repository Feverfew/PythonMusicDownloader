﻿from PySide import QtCore, QtGui

class MainWindowView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(606, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(606, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 606, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_AS = QtGui.QAction(MainWindow)
        self.actionSave_AS.setObjectName("actionSave_AS")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Program = QtGui.QAction(MainWindow)
        self.actionAbout_Program.setObjectName("actionAbout_Program")
        self.actionAbout_Author = QtGui.QAction(MainWindow)
        self.actionAbout_Author.setObjectName("actionAbout_Author")
        self.actionDocs = QtGui.QAction(MainWindow)
        self.actionDocs.setObjectName("actionDocs")
        self.actionTutorial = QtGui.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionReport_a_Bug = QtGui.QAction(MainWindow)
        self.actionReport_a_Bug.setObjectName("actionReport_a_Bug")
        self.menuAbout.addAction(self.actionAbout_Program)
        self.menuAbout.addAction(self.actionAbout_Author)
        self.menuHelp.addAction(self.actionReport_a_Bug)
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Music Downloader", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save ", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_AS.setText(QtGui.QApplication.translate("MainWindow", "Save AS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Program.setText(QtGui.QApplication.translate("MainWindow", "About Program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Author.setText(QtGui.QApplication.translate("MainWindow", "About Author", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDocs.setText(QtGui.QApplication.translate("MainWindow", "Docs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTutorial.setText(QtGui.QApplication.translate("MainWindow", "Tutorial", None, QtGui.QApplication.UnicodeUTF8))
        self.actionReport_a_Bug.setText(QtGui.QApplication.translate("MainWindow", "Report a Bug", None, QtGui.QApplication.UnicodeUTF8))




class TrackDownloaderView(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(606, 583)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.artist_label = QtGui.QLabel(Form)
        self.artist_label.setObjectName("artist_label")
        self.horizontalLayout_3.addWidget(self.artist_label)
        self.artist_field = QtGui.QLineEdit(Form)
        self.artist_field.setMinimumSize(QtCore.QSize(0, 25))
        self.artist_field.setObjectName("artist_field")
        self.horizontalLayout_3.addWidget(self.artist_field)
        self.track_label = QtGui.QLabel(Form)
        self.track_label.setObjectName("track_label")
        self.horizontalLayout_3.addWidget(self.track_label)
        self.track_field = QtGui.QLineEdit(Form)
        self.track_field.setMinimumSize(QtCore.QSize(0, 25))
        self.track_field.setObjectName("track_field")
        self.horizontalLayout_3.addWidget(self.track_field)
        self.quality_lbl = QtGui.QLabel(Form)
        self.quality_lbl.setObjectName("quality_lbl")
        self.horizontalLayout_3.addWidget(self.quality_lbl)
        self.quality_combobox = QtGui.QComboBox(Form)
        self.quality_combobox.setMinimumSize(QtCore.QSize(0, 27))
        self.quality_combobox.setMinimumContentsLength(0)
        self.quality_combobox.setObjectName("quality_combobox")
        self.quality_combobox.addItem("")
        self.quality_combobox.addItem("")
        self.quality_combobox.addItem("")
        self.quality_combobox.addItem("")
        self.horizontalLayout_3.addWidget(self.quality_combobox)
        self.search_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy)
        self.search_btn.setMinimumSize(QtCore.QSize(100, 27))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.results_table = QtGui.QTableWidget(Form)
        self.results_table.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_table.sizePolicy().hasHeightForWidth())
        self.results_table.setSizePolicy(sizePolicy)
        self.results_table.setAutoFillBackground(False)
        self.results_table.setFrameShadow(QtGui.QFrame.Sunken)
        self.results_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.results_table.setWordWrap(False)
        self.results_table.setObjectName("results_table")
        self.results_table.setColumnCount(5)
        self.results_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(4, item)
        self.horizontalLayout_4.addWidget(self.results_table)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.skip_to_field = QtGui.QLineEdit(Form)
        self.skip_to_field.setMinimumSize(QtCore.QSize(0, 25))
        self.skip_to_field.setObjectName("skip_to_field")
        self.horizontalLayout.addWidget(self.skip_to_field)
        self.skip_to_btn = QtGui.QPushButton(Form)
        self.skip_to_btn.setMinimumSize(QtCore.QSize(0, 27))
        self.skip_to_btn.setObjectName("skip_to_btn")
        self.horizontalLayout.addWidget(self.skip_to_btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.prev_page_btn = QtGui.QPushButton(Form)
        self.prev_page_btn.setMinimumSize(QtCore.QSize(0, 27))
        self.prev_page_btn.setObjectName("prev_page_btn")
        self.horizontalLayout.addWidget(self.prev_page_btn)
        self.next_page_btn = QtGui.QPushButton(Form)
        self.next_page_btn.setMinimumSize(QtCore.QSize(0, 27))
        self.next_page_btn.setObjectName("next_page_btn")
        self.horizontalLayout.addWidget(self.next_page_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.download_dir_label = QtGui.QLabel(Form)
        self.download_dir_label.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_dir_label.sizePolicy().hasHeightForWidth())
        self.download_dir_label.setSizePolicy(sizePolicy)
        self.download_dir_label.setObjectName("download_dir_label")
        self.horizontalLayout_5.addWidget(self.download_dir_label)
        self.download_dir_field = QtGui.QLineEdit(Form)
        self.download_dir_field.setEnabled(False)
        self.download_dir_field.setMinimumSize(QtCore.QSize(0, 25))
        self.download_dir_field.setObjectName("download_dir_field")
        self.horizontalLayout_5.addWidget(self.download_dir_field)
        self.download_dir_btn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.download_dir_btn.sizePolicy().hasHeightForWidth())
        self.download_dir_btn.setSizePolicy(sizePolicy)
        self.download_dir_btn.setMinimumSize(QtCore.QSize(100, 27))
        self.download_dir_btn.setObjectName("download_dir_btn")
        self.horizontalLayout_5.addWidget(self.download_dir_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.download_btn = QtGui.QPushButton(Form)
        self.download_btn.setMinimumSize(QtCore.QSize(100, 27))
        self.download_btn.setObjectName("download_btn")
        self.horizontalLayout_6.addWidget(self.download_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.artist_label.setText(QtGui.QApplication.translate("Form", "Artist: ", None, QtGui.QApplication.UnicodeUTF8))
        self.track_label.setText(QtGui.QApplication.translate("Form", "Track:", None, QtGui.QApplication.UnicodeUTF8))
        self.quality_lbl.setText(QtGui.QApplication.translate("Form", "Quality", None, QtGui.QApplication.UnicodeUTF8))
        self.quality_combobox.setItemText(0, QtGui.QApplication.translate("Form", "All", None, QtGui.QApplication.UnicodeUTF8))
        self.quality_combobox.setItemText(1, QtGui.QApplication.translate("Form", "Best", None, QtGui.QApplication.UnicodeUTF8))
        self.quality_combobox.setItemText(2, QtGui.QApplication.translate("Form", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.quality_combobox.setItemText(3, QtGui.QApplication.translate("Form", "Low", None, QtGui.QApplication.UnicodeUTF8))
        self.search_btn.setText(QtGui.QApplication.translate("Form", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.results_table.setSortingEnabled(True)
        self.results_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Artist", None, QtGui.QApplication.UnicodeUTF8))
        self.results_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Track", None, QtGui.QApplication.UnicodeUTF8))
        self.results_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.results_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "Bitrate", None, QtGui.QApplication.UnicodeUTF8))
        self.results_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "Id", None, QtGui.QApplication.UnicodeUTF8))
        self.skip_to_btn.setText(QtGui.QApplication.translate("Form", "Skip to Page", None, QtGui.QApplication.UnicodeUTF8))
        self.prev_page_btn.setText(QtGui.QApplication.translate("Form", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.next_page_btn.setText(QtGui.QApplication.translate("Form", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.download_dir_label.setText(QtGui.QApplication.translate("Form", "Download Directory: ", None, QtGui.QApplication.UnicodeUTF8))
        self.download_dir_btn.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.download_btn.setText(QtGui.QApplication.translate("Form", "Download", None, QtGui.QApplication.UnicodeUTF8))






