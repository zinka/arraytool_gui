# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sat Mar 18 12:08:47 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(451, 272)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        self.verticalLayout_8.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.textBrowser_2 = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_13.addWidget(self.textBrowser_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_13)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_15 = QtGui.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.textBrowser_3 = QtGui.QTextBrowser(self.tab_3)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_15.addWidget(self.textBrowser_3)
        self.verticalLayout_14.addLayout(self.verticalLayout_15)
        self.verticalLayout_5.addLayout(self.verticalLayout_14)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_16 = QtGui.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_17 = QtGui.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.textBrowser_4 = QtGui.QTextBrowser(self.tab_4)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.verticalLayout_17.addWidget(self.textBrowser_4)
        self.verticalLayout_16.addLayout(self.verticalLayout_17)
        self.verticalLayout_6.addLayout(self.verticalLayout_16)
        self.verticalLayout_11.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_18 = QtGui.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.textBrowser_5 = QtGui.QTextBrowser(self.tab_5)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.verticalLayout_19.addWidget(self.textBrowser_5)
        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        self.verticalLayout_7.addLayout(self.verticalLayout_18)
        self.verticalLayout_12.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Arraytool Version 0.1.0</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(18 March 2017)</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Built from git commit hash </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Library directory: /usr/share/arraytool/</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User directory: ~/.arraytool/</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Qt Version (run-time): 4.8.7</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Qt Version (compile-time): 4.8.7</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Srinivasa Rao Zinka</span><br /><span style=\" font-style:italic;\">E-mail: srinivas.zinka@gmail.com</span><br />Author of the Arraytool library</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Credits", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_3.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">BSD 3-Clause License</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (c) 2017, Srinivasa Rao Zinka</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All rights reserved.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Redistributions of source code must retain the above copyright notice, this   list of conditions and the following disclaimer.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Redistributions in binary form must reproduce the above copyright notice,   this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">* Neither the name of the copyright holder nor the names of its  contributors may be used to endorse or promote products derived from  this software without specific prior written permission.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "Copyright", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_4.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Dialog", "Build Info", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser_5.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:x-large; font-weight:600;\">Important Changes in Arraytool 0.1.0</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\">This is the first version that we are releasing. This section will be updated in future releases.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("Dialog", "Release Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

