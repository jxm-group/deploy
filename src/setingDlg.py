#/usr/bin/env python
#coding=utf-8

from PyQt4.QtCore import pyqtSlot

from setingDlg_qss import SetingDlg_Qss
import json

class SetingDlg(SetingDlg_Qss):
    def __init__(self,parent = None):
        super(SetingDlg, self).__init__(parent)
        self.setModal(True)

        fd = open("./cfg.json")
        cfg_string =  fd.read()
        fd.close()
        self.__cfg_json = json.loads(cfg_string)

        print (cfg_string)
        print(self.__cfg_json)

        self.lineEditDhcpServerIp.setText(
           self.__cfg_json["DHCP_SERVER_IP"]
        )
        self.lineEditDhcpOfferBegin.setText(
            self.__cfg_json["DHCP_OFFER_BEGIN"]
        )
        self.lineEditDhcpOfferEnd.setText(
            self.__cfg_json["DHCP_OFFER_END"]
        )
        self.lineEditDhcpSubnet.setText(
            self.__cfg_json["DHCP_SUBNET"]
        )
        self.lineEditDhcpDns.setText(
            self.__cfg_json["DHCP_DNS"]
        )

    @pyqtSlot()
    def on_saveBtn_clicked(self):
        print "on_saveBtn_clicked ---"

    @pyqtSlot()
    def on_cancleBtn_clicked(self): # 选择目录
        print "on_cancleBtn_clicked ---"

if __name__ ==  "__main__":
    from PyQt4.QtGui import QApplication
    import sys

    app = QApplication(sys.argv)
    mainWindow = SetingDlg()
    mainWindow.show()
    sys.exit(app.exec_())
