#/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import SIGNAL, QString

from PyQt4.QtGui import QDialog, QFileDialog
from PyQt4.QtGui import QLineEdit,QPushButton
from PyQt4.QtGui import QVBoxLayout,QHBoxLayout

class MainWindow(QDialog):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)

        self.__lineEditFileName = QLineEdit()
        self.__selectFileBtn = QPushButton(self.tr("select File"))

        self.__lineEditFileDir = QLineEdit()
        self.__selectFileDirBtn = QPushButton(self.tr("select Dir"))

        hboxlayout_fileName = QHBoxLayout()
        hboxlayout_fileName.addWidget(self.__lineEditFileName)
        hboxlayout_fileName.addWidget(self.__selectFileBtn)

        hboxlayout_fileDir = QHBoxLayout()
        hboxlayout_fileDir.addWidget(self.__lineEditFileDir)
        hboxlayout_fileDir.addWidget(self.__selectFileDirBtn)

        vboxlayout = QVBoxLayout(self)
        vboxlayout.addLayout(hboxlayout_fileName)
        vboxlayout.addLayout(hboxlayout_fileDir)

        self.connect(self.__selectFileBtn,SIGNAL("clicked()"),self.soltFile)
        self.connect(self.__selectFileDirBtn,SIGNAL("clicked()"),self.soltFileDir)

    def soltFile(self):
        fileName = QFileDialog.getOpenFileName()
        # print fileName
        self.__lineEditFileName.setText(str(fileName.toAscii()))


    def soltFileDir(self): # 选择目录
        fileName = QFileDialog.getExistingDirectory()
        # print fileName
        self.__lineEditFileDir.setText(str(fileName.toAscii()))

if __name__ ==  "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
