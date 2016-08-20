#coding=utf-8
import os

from PyQt4.QtCore import QThread, SIGNAL,QTextCodec
from PyQt4.QtGui import QTextBrowser
from PyQt4.QtCore import QString
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QProgressBar
from PyQt4.QtGui import QVBoxLayout,QHBoxLayout

from decompressionThread import DecompressionThread,CompressionThread

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.setFixedSize(600, 300)
        self.move(200, 200)


        self.__progressBar = QProgressBar()

        self.decompressionShow  =  QTextBrowser(self)

        vboxLayout = QVBoxLayout(self)
        vboxLayout.addWidget(self.__progressBar)
        vboxLayout.addWidget(self.decompressionShow)


        import sys
        if os.name == 'posix' and sys.version_info[0] < 3:
            TAR_PATH = '/tmp/testTar/abc.tar'   #tar文件存放位置
            EXT_PATH = '/tmp/test/tmp'  #取出文件存放目录
        else:
            TAR_PATH = 'f:\\testTar\\hongten.tar'   #tar文件存放位置
            EXT_PATH = 'f:\\test\\tmp'  #取出文件存放目录

        try:
            _path = os.path.dirname(TAR_PATH)
            print _path
            os.makedirs(_path)
            os.makedirs(EXT_PATH)
        except Exception:
            pass


        self.__compressionThread = CompressionThread(TAR_PATH)
        self.__compressionThread.start()
        self.__compressionThread.wait()

        self.__decompressionThread = DecompressionThread(TAR_PATH,EXT_PATH)

        self.connect(self.__decompressionThread, SIGNAL("Decompression_Log"), self.testPrint)

    def testPrint(self, log,process):
        print  "testPrint:", log
        self.decompressionShow.append(QString(log))
        # process = {
        #     "status" :  False,
        #     "total"  :  total,
        #     "count"  :  count,
        # }
        if process["status"] == True:
            self.close()

        if process["total"] > 0:
            self.__progressBar.setRange(0,process["total"])

            self.__progressBar.setValue(process["count"])


    def startDecTest(self):
        self.__decompressionThread.start()


if __name__ == "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')
    QTextCodec.setCodecForCStrings(QTextCodec.codecForLocale())
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    dlg.startDecTest()

    sys.exit(app.exec_())
