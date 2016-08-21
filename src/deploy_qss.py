#/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import SIGNAL, QString

from PyQt4.QtGui import QDialog, QFileDialog
from PyQt4.QtGui import QLineEdit,QPushButton
from PyQt4.QtGui import QVBoxLayout,QHBoxLayout
from PyQt4.QtCore import QMetaObject,pyqtSlot

class Deploy_Qss(QDialog):
    def __init__(self,parent = None):
        super(Deploy_Qss, self).__init__(parent)

        self.__tar_file =  None
        self.__lineEditFileName = QLineEdit()
        self.__selectFileBtn = QPushButton(self.tr("select File"))  # 选择解压文件
        self.__selectFileBtn.setObjectName("selectFileBtn")

        self.__lineEditFileDir = QLineEdit()
        self.__selectFileDirBtn = QPushButton(self.tr("select Dir")) # 选择解压目录
        self.__selectFileDirBtn.setObjectName("selectFileDirBtn")

        self.__setingBtn  = QPushButton(self.tr("seting"))
        self.__setingBtn.setObjectName("setingBtn")
        self.__decBtn  = QPushButton(self.tr("decompression"))
        self.__decBtn.setObjectName("decBtn")

        self.__tftpServerStartBtn = QPushButton(self.tr("tftp server start"))
        self.__tftpServerStartBtn.setObjectName("tftpServerStartBtn")
        self.__tftpServerStopBtn  = QPushButton(self.tr("tftp server stop"))
        self.__tftpServerStopBtn.setObjectName("tftpServerStopBtn")

        hboxlayout_fileName = QHBoxLayout()
        hboxlayout_fileName.addWidget(self.__lineEditFileName)
        hboxlayout_fileName.addWidget(self.__selectFileBtn)

        hboxlayout_fileDir = QHBoxLayout()
        hboxlayout_fileDir.addWidget(self.__lineEditFileDir)
        hboxlayout_fileDir.addWidget(self.__selectFileDirBtn)

        hboxlayout_setting= QHBoxLayout()
        hboxlayout_setting.addWidget(self.__setingBtn)
        hboxlayout_setting.addWidget(self.__decBtn)

        hboxlayout_tftpServerBtn= QHBoxLayout()
        hboxlayout_tftpServerBtn.addWidget(self.__tftpServerStartBtn)
        hboxlayout_tftpServerBtn.addWidget(self.__tftpServerStopBtn)


        vboxlayout = QVBoxLayout(self)
        vboxlayout.addLayout(hboxlayout_fileName)
        vboxlayout.addLayout(hboxlayout_fileDir)
        vboxlayout.addLayout(hboxlayout_setting)
        vboxlayout.addLayout(hboxlayout_tftpServerBtn)

        QMetaObject.connectSlotsByName(self)


    # 选择　压缩文件
    @pyqtSlot()
    def on_selectFileBtn_clicked(self):
        print "on_selectFileBtn_clicked"

    # 选择　 解压目录
    @pyqtSlot()
    def on_selectFileDirBtn_clicked(self): # 选择目录
        print "soltFileDir_clicked"

    # 选择　 解压目录
    @pyqtSlot()
    def on_setingBtn_clicked(self): # 选择目录
        print "on_setingBtn_clicked"

    # 选择　 解压目录
    @pyqtSlot()
    def on_decBtn_clicked(self): # 选择目录
        print "on_decBtn_clicked"

    # 选择　 解压目录
    @pyqtSlot()
    def on_tftpServerStartBtn_clicked(self): # 选择目录
        print "on_tftpServerStartBtn_clicked"

    # 选择　 解压目录
    @pyqtSlot()
    def on_tftpServerStopBtn_clicked(self): # 选择目录
        print "on_tftpServerStopBtn_clicked"

if __name__ ==  "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)
    mainWindow = Deploy_Qss()
    mainWindow.show()
    sys.exit(app.exec_())
