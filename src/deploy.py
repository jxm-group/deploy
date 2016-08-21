#/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import  pyqtSlot

from PyQt4.QtGui import  QFileDialog
from decompressionDlg import DecompressionDlg

from deploy_qss import Deploy_Qss
from setingDlg import SetingDlg

class MainWindow(Deploy_Qss):
    def __init__(self,parent = None):
        super(MainWindow, self).__init__(parent)
        self.__decompressdlg = DecompressionDlg()
        self.__setingDlg    = SetingDlg()

    # 选择　压缩文件
    @pyqtSlot()
    def on_selectFileBtn_clicked(self):
        print "on_selectFileBtn_clicked"
        fileName = QFileDialog.getOpenFileName()
        self._Deploy_Qss__lineEditFileName.setText(str(fileName.toAscii()))

    # 选择　 解压目录
    @pyqtSlot()
    def on_selectFileDirBtn_clicked(self): # 选择目录
        print "soltFileDir_clicked"
        fileName = QFileDialog.getExistingDirectory()
        self._Deploy_Qss__lineEditFileDir.setText(str(fileName.toAscii()))

    @pyqtSlot()
    def on_setingBtn_clicked(self):
        print "on_setingBtn_clicked"
        self.__setingDlg.show()

    @pyqtSlot()
    def on_decBtn_clicked(self):  # 解压
        print "on_decBtn_clicked"
        self.__decompressdlg.show()
        self.__decompressdlg.startDec()

    @pyqtSlot()
    def on_tftpServerStartBtn_clicked(self):
        print "on_tftpServerStartBtn_clicked"

    @pyqtSlot()
    def on_tftpServerStopBtn_clicked(self):
        print "on_tftpServerStopBtn_clicked"


if __name__ ==  "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
