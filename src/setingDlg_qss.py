#/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import SIGNAL, QString, QRegExp

from PyQt4.QtGui import QDialog, QFileDialog, QLabel, QRegExpValidator
from PyQt4.QtGui import QLineEdit,QPushButton
from PyQt4.QtGui import QVBoxLayout,QHBoxLayout,QGridLayout
from PyQt4.QtCore import QMetaObject,pyqtSlot

class SetingDlg_Qss(QDialog):
    def __init__(self,parent = None):
        super(SetingDlg_Qss, self).__init__(parent)

        reg = QRegExp('^((\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])\\.){3}(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-4])$')
        # reg=QRegExp('^[0-9\.]{0,15}$')
        validator = QRegExpValidator(reg)


        self.__labelDhcpServerIp = QLabel(self.tr("DHCP_SERVER_IP"))
        self.lineEditDhcpServerIp = QLineEdit()
        self.lineEditDhcpServerIp.setValidator(validator)

        self.__labelDhcpOfferBegin = QLabel(self.tr("DHCP_OFFER_BEGIN"))
        self.lineEditDhcpOfferBegin = QLineEdit()
        self.lineEditDhcpOfferBegin.setValidator(validator)


        self.__labelDhcpOfferEnd = QLabel(self.tr("DHCP_OFFER_END"))
        self.lineEditDhcpOfferEnd = QLineEdit()
        self.lineEditDhcpOfferEnd.setValidator(validator)

        self.__labelDhcpSubnet = QLabel(self.tr("DHCP_SUBNET"))
        self.lineEditDhcpSubnet = QLineEdit()
        self.lineEditDhcpSubnet.setValidator(validator)

        self.__labelDhcpRouter = QLabel(self.tr("DHCP_ROUTER"))
        self.lineEditDhcpRouter = QLineEdit()
        self.lineEditDhcpRouter.setValidator(validator)

        self.__labelDhcpDns = QLabel(self.tr("DHCP_DNS"))
        self.lineEditDhcpDns = QLineEdit()
        self.lineEditDhcpDns.setValidator(validator)

        gridLayout = QGridLayout()
        lableCol = 0
        lineEditCol = 1
        gridLayout.addWidget(self.__labelDhcpServerIp,0,lableCol)
        gridLayout.addWidget(self.lineEditDhcpServerIp,0,lineEditCol)

        gridLayout.addWidget(self.__labelDhcpOfferBegin,1,lableCol)
        gridLayout.addWidget(self.lineEditDhcpOfferBegin,1,lineEditCol)

        gridLayout.addWidget(self.__labelDhcpOfferEnd,2,lableCol)
        gridLayout.addWidget(self.lineEditDhcpOfferEnd,2,lineEditCol)

        gridLayout.addWidget(self.__labelDhcpSubnet,3,lableCol)
        gridLayout.addWidget(self.lineEditDhcpSubnet,3,lineEditCol)

        gridLayout.addWidget(self.__labelDhcpDns,4,lableCol)
        gridLayout.addWidget(self.lineEditDhcpDns,4,lineEditCol)


        self.__saveBtn = QPushButton(self.tr("save"))
        self.__saveBtn.setObjectName("saveBtn")
        self.__cancleBtn = QPushButton(self.tr("cancle"))
        self.__cancleBtn.setObjectName("cancleBtn")

        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.__saveBtn)
        hboxLayout.addWidget(self.__cancleBtn)

        vboxLayout = QVBoxLayout(self)
        vboxLayout.addLayout(gridLayout)
        vboxLayout.addLayout(hboxLayout)


        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_saveBtn_clicked(self):
        print "on_saveBtn_clicked"

    @pyqtSlot()
    def on_cancleBtn_clicked(self): # 选择目录
        print "on_cancleBtn_clicked"

if __name__ ==  "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)
    mainWindow = SetingDlg_Qss()
    mainWindow.show()
    sys.exit(app.exec_())
