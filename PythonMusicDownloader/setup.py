from cx_Freeze import setup, Executable

exe=Executable(
     script="PythonMusicDownloader.py",
     base="Win32Gui",
     icon="resources/icon.ico"
     )
includefiles=["controllers.py","models.py","views.py"]
includes=[]
excludes=[]
packages=["requests", "atexit", "Pyside"]
setup(

     version = "0.1",
     description = "Beta release of Music Downloader written in Python",
     author = "Alexander saoutkin",
     name = "Music Downloader",
     options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
     )