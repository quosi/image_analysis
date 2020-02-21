#plugin
print("copy plugins")
os.system&#40;"cp -r plugins dist/test.app/Contents/PlugIns"&#41;
os.system("cp qt.conf dist/test.app/Contents/Resources/qt.conf"&#41; 

# (4&#41; correct dylib references

appPath = "PATH_TO_YOUR_APP"
qtPath = "PATH_TO_QT_LIB"
pythonPath = "PATH_TO_PYTHON"

def iid(dylib):
    command = "install_name_tool -id @executable_path/../PlugIns/{dylib} {appPath}/Contents/PlugIns/{dylib}".format(dylib=dylib, appPath=appPath)
    os.system&#40;command&#41;

def icPython(dylib&#41;:
    command = "install_name_tool -change {pythonPath}/Python.framework/Versions/3.3/Python @executable_path/../Frameworks/Python.framework/Versions/3.3/Python {appPath}/Contents/PlugIns/{dylib}".format(dylib=dylib, appPath=appPath, pythonPath=pythonPath)
    os.system&#40;command&#41;
    
def icCore(dylib&#41;:
    command = "install_name_tool -change {qtPath}/lib/QtCore.framework/Versions/5/QtCore @executable_path/../Frameworks/QtCore.framework/Versions/5/QtCore {appPath}/Contents/PlugIns/{dylib}".format(dylib=dylib, appPath=appPath, qtPath=qtPath)
    os.system&#40;command&#41;

....

def update(dylib&#41;:
    iid(dylib)
    icPython(dylib)
    icCore(dylib)
    ....

#accessible
print("# update accessible")
update("accessible/libqtaccessiblequick.dylib")
update("accessible/libqtaccessiblewidgets.dylib")

#bearer
print("# update bearer")
update("bearer/libqcorewlanbearer.dylib")
....

#platform
print("# update platforms")
update("platforms/libqcocoa.dylib")   ## <-- you need it
update("platforms/libqminimal.dylib")

print("DEPLOY")
for path in QApplication.libraryPaths():
QApplication.removeLibraryPath(path)

filePath = os.path.dirname(os.path.abspath( __file__ )) 
# abspath returns "APP_DIR/Contents/Resouces". This isn't same to C++ app.
fileDir = QDir(filePath)
fileDir.cdUp()
fileDir.cd("PlugIns")
appPath = fileDir.absolutePath()
QApplication.addLibraryPath(str(appPath))

print("INIT: " + str(QApplication.libraryPaths()))
app = QApplication(sys.argv)

