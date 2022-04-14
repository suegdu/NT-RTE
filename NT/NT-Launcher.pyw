import os
import time
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
from requests import get
import sys
from pathlib import Path
BOOTLegContent = """
"""



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 492)
        MainWindow.setWhatsThis("")
        MainWindow.setWindowFilePath("")
        self.__basedversion__ = "NT PT Build 1.3"
        self.__basedlauncher__ = "PTC 1.0"
        self.__basedpt__ = "Launch NT 1.0"
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 721, 431))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 20, 261, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 221, 211))
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBox_debugmode = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_debugmode.setGeometry(QtCore.QRect(10, 20, 121, 17))
        self.checkBox_debugmode.setObjectName("checkBox_debugmode")
        self.checkBox_temploader = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_temploader.setGeometry(QtCore.QRect(10, 40, 91, 17))
        self.checkBox_temploader.setObjectName("checkBox_temploader")
        self.checkBox_customloader = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_customloader.setEnabled(False)
        self.checkBox_customloader.setGeometry(QtCore.QRect(10, 60, 171, 17))
        self.checkBox_customloader.setObjectName("checkBox_customloader")
        self.label_nothingfornow = QtWidgets.QLabel(self.groupBox_6)
        self.label_nothingfornow.setGeometry(QtCore.QRect(70, 140, 151, 16))
        self.label_nothingfornow.setTextFormat(QtCore.Qt.AutoText)
        self.label_nothingfornow.setScaledContents(False)
        self.label_nothingfornow.setWordWrap(False)
        self.label_nothingfornow.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.label_nothingfornow.setObjectName("label_nothingfornow")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 240, 221, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_reset = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_restorefiles = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_restorefiles.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.pushButton_restorefiles.setObjectName("pushButton_restorefiles")
        self.pushButton_verifyfiles = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_verifyfiles.setGeometry(QtCore.QRect(10, 80, 75, 23))
        self.pushButton_verifyfiles.setObjectName("pushButton_verifyfiles")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setGeometry(QtCore.QRect(90, 20, 171, 20))
        self.label_2.setLineWidth(1)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_7)
        self.label_3.setGeometry(QtCore.QRect(90, 50, 151, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_7)
        self.label_4.setGeometry(QtCore.QRect(90, 80, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 100, 231, 31))
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 210, 431, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_github = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_github.setGeometry(QtCore.QRect(350, 130, 75, 23))
        self.pushButton_github.setObjectName("pushButton_github")
        self.pushButton_updates = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_updates.setGeometry(QtCore.QRect(350, 100, 75, 23))
        self.pushButton_updates.setObjectName("pushButton_updates")
        self.textBrowser_notablechanges = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_notablechanges.setGeometry(QtCore.QRect(10, 20, 331, 131))
        self.textBrowser_notablechanges.setObjectName("textBrowser_notablechanges")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 431, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_launchstart = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_launchstart.setGeometry(QtCore.QRect(20, 20, 101, 23))
        self.pushButton_launchstart.setObjectName("pushButton_launchstart")
        self.textBrowser_statuslogstart = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_statuslogstart.setGeometry(QtCore.QRect(20, 70, 241, 111))
        self.textBrowser_statuslogstart.setObjectName("textBrowser_statuslogstart")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(20, 50, 111, 16))
        self.label.setObjectName("label")
        self.label_note1 = QtWidgets.QLabel(self.groupBox_4)
        self.label_note1.setGeometry(QtCore.QRect(270, 70, 171, 51))
        self.label_note1.setObjectName("label_note1")
        self.label_note22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_note22.setGeometry(QtCore.QRect(270, 130, 161, 31))
        self.label_note22.setObjectName("label_note22")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar.setGeometry(QtCore.QRect(260, 20, 161, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 370, 431, 51))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_launcherversion = QtWidgets.QLabel(self.groupBox_5)
        self.label_launcherversion.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.label_launcherversion.setObjectName("label_launcherversion")
        self.label_ntversion = QtWidgets.QLabel(self.groupBox_5)
        self.label_ntversion.setGeometry(QtCore.QRect(200, 20, 111, 16))
        self.label_ntversion.setObjectName("label_ntversion")
        self.label_PTCversion = QtWidgets.QLabel(self.groupBox_5)
        self.label_PTCversion.setGeometry(QtCore.QRect(320, 20, 131, 16))
        self.label_PTCversion.setObjectName("label_PTCversion")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 440, 631, 16))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_launchstart.clicked.connect(self.Sidelaunching)
        self.pushButton_github.clicked.connect(self.openinghub)
        self.pushButton_updates.clicked.connect(self.tempupdates)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NT Launcher 1.0"))
        self.groupBox.setTitle(_translate("MainWindow", "Launcher"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
        self.groupBox_6.setTitle(_translate("MainWindow", "NT "))
        self.checkBox_debugmode.setText(_translate("MainWindow", "Debug Mode"))
        self.checkBox_temploader.setText(_translate("MainWindow", "Temp Loader"))
        self.checkBox_customloader.setText(_translate("MainWindow", "Load Custom Extensions"))
        self.label_nothingfornow.setText(_translate("MainWindow", "Nohting For Now"))
        self.groupBox_7.setTitle(_translate("MainWindow", "System"))
        self.pushButton_reset.setText(_translate("MainWindow", "Reset"))
        self.pushButton_restorefiles.setText(_translate("MainWindow", "Restore Files"))
        self.pushButton_verifyfiles.setText(_translate("MainWindow", "Verify Files"))
        self.label_2.setText(_translate("MainWindow", "Will Reset Everything"))
        self.label_3.setText(_translate("MainWindow", "Restore The Missing Files"))
        self.label_4.setText(_translate("MainWindow", "Verify Files."))
        self.label_5.setText(_translate("MainWindow", "NOTE: Watch The \"Status Log\" To Be \n"
"Informed About The Prcoess."))
        self.groupBox_3.setTitle(_translate("MainWindow", "NotAbleChanges"))
        self.pushButton_github.setText(_translate("MainWindow", "Github"))
        self.pushButton_updates.setText(_translate("MainWindow", "Updates"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Start"))
        self.pushButton_launchstart.setText(_translate("MainWindow", f"{self.__basedpt__}"))
        self.textBrowser_statuslogstart.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Status Log :"))
        self.label_note1.setText(_translate("MainWindow", "NOTE: Some Settings Wont Be\n"
" Applied In Action Until You \n"
"Restart NT Or Faced \n"
"A Force Boot Side."))
        self.label_note22.setText(_translate("MainWindow", "NOTE: The Debug Mode May \n"
"Cost Some Bugs And Hanging."))
        self.groupBox_5.setTitle(_translate("MainWindow", "Information"))
        self.label_launcherversion.setText(_translate("MainWindow", f"Launcher Version : {self.__basedlauncher__}"))
        self.label_ntversion.setText(_translate("MainWindow", f"NT Version : {self.__basedversion__}"))
        self.label_PTCversion.setText(_translate("MainWindow", "PTC Version : 1.7.54"))
        self.label_7.setText(_translate("MainWindow", "Author : suegdu | suegdu Github. do not disturb!.  NT Are Licensed Under The Creative Commons Zero v1.0 Universal License."))

    def NTworker(self):
        
        self.statusinsertor(f"{self.__basedversion__} | {self.__basedlauncher__} Started. {time.time()}")
        self.statusinsertor("NOTE: You started NT through the launcher and thats right because if you did run it through the main file manually some changes wont be applied or even works propely.")
        try:

         os.startfile(Path(__file__).with_name("NTbootleg.py"))
         
        except FileNotFoundError:
            with open("NTbootleg.py", "a") as NTBOOTLeg:
                NTBOOTLeg.write()



    
        
        

    def statusinsertor(self,message):
        self.textBrowser_statuslogstart.insertPlainText(message+"\n")
    def tempupdates(self):
        webbrowser.open("https://github.com/suegdu/NT-RTE/releases")
    def openinghub(self):
        webbrowser.open("https://github.com/suegdu/NT-RTE")
    
    
    
    
    
    
    
    def Sidelaunching(self):
        self.PORstarting()
        self.NTworker()
        self.PORstopper()

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
        

    
    def PORstopper(self):
        self.progressBar.setProperty("value",0)

    
        
    def PORstarting(self):
        for i in range(99):
            time.sleep(00.001)
            self.progressBar.setProperty("value", i+1)


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)        
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    {
        ui.setupUi(MainWindow),
        MainWindow.show(),
        sys.exit(app.exec_())

    }
    
    
    








