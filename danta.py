import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from Kiwoom import *

form_class = uic.loadUiType("danta.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.kiwoom=Kiwoom()
        self.kiwoom.comm_connect()
        self.lineEdit_event.textChanged.connect(self.code_changed)

        accouns_num = int(self.kiwoom.get_login_info("ACCOUNT_CNT"))
        accounts = self.kiwoom.get_login_info("ACCNO")
aa
        accounts_list = accounts.split(';')[0:accouns_num]
        self.comboBox_account.addItems(accounts_list)

        self.pushButton.clicked.connect(self.send_order)

    def code_changed(self):
        code = self.lineEdit_event.text()
        name = self.kiwoom.get_master_code_name(code)
        self.lineEdit_event_name.setText(name)

    def send_order(self):
        order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
        hoga_lookup = {'지정가': "00", '시장가': "03"}

        account = self.comboBox_account.currentText()
        order_type = self.comboBox_order.currentText()
        code = self.lineEdit_event.text()
        hoga = self.comboBox_kinds.currentText()
        num = self.spinBox_quantity.value()
        price = self.spinBox_price.value()

        self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price,
                               hoga_lookup[hoga], "")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
