############################################################################
#
#   "Gngr request" project
#   © 2021 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2021
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
from PyQt5 import QtWidgets, QtGui, uic
import json, ast, sys, RequestsFunction



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()

        uic.loadUi('Gngr_requests_qui.ui', self)
        self.setWindowIcon(QtGui.QIcon('Gngr_requests.ico'))
        #
        self.combobox_proxy = self.findChild(QtWidgets.QComboBox, name="proxy_input")
        proxy_list = RequestsFunction.get_proxy_list()
        for proxy in  proxy_list:
            self.combobox_proxy.addItem(proxy)
        #
        self.button_gonder = self.findChild(QtWidgets.QPushButton, name='gonder')
        self.button_gonder.clicked.connect(self.button_func_gonder)
        #
        self.button_temizle = self.findChild(QtWidgets.QPushButton, name='temizle')
        self.button_temizle.clicked.connect(self.button_func_temizle)
        #
        self.show()

    #
    def button_func_gonder(self):
        try:
            #
            data = RequestsFunction.RequestData()
            data.input_url = (self.findChild(QtWidgets.QLineEdit, name='url_input')).text()
            data.input_type = (self.findChild(QtWidgets.QComboBox, name='method_input')).currentText()
            #
            proxy = (self.findChild(QtWidgets.QComboBox, name='proxy_input')).currentText()
            proxies = None
            if proxy != "HAYIR":
                proxies = { 'http': proxy,
                            'https': proxy}
            data.input_proxies = proxies
            #
            data.input_timeout = float( (self.findChild(QtWidgets.QLineEdit, name='timeout_input')).text() )
            #
            headers = dict()
            headers_str = str((self.findChild(QtWidgets.QPlainTextEdit, name='headers_input')).toPlainText()).split('\n')
            for tmp in headers_str:
                tmp = tmp.strip()
                if tmp != '':
                    tmp_dict = ast.literal_eval(tmp)
                    headers.update(tmp_dict)
            if (len(headers) > 0):
                data.input_headers = headers
            #
            params = dict()
            params_str = str((self.findChild(QtWidgets.QPlainTextEdit, name='params_input')).toPlainText()).split('\n')
            for tmp in params_str:
                tmp = tmp.strip()
                if tmp != '':
                    tmp_dict = ast.literal_eval(tmp)
                    params.update(tmp_dict)
            if (len(params) > 0):
                data.input_params = params
            #
            form = dict()
            form_str = str((self.findChild(QtWidgets.QPlainTextEdit, name='form_input')).toPlainText()).split('\n')
            for tmp in form_str:
                tmp = tmp.strip()
                if tmp != '':
                    tmp_dict = ast.literal_eval(tmp)
                    form.update(tmp_dict)
            if (len(form) > 0):
                data.input_form = form
            #
            json_str = str((self.findChild(QtWidgets.QPlainTextEdit, name='json_input')).toPlainText())
            if json_str != '':
                data.input_json = json.loads(json_str)
            #
            #
            data = RequestsFunction.url_function(data=data)
            #
            #
            self.button_func_temizle()
            #
            if not data.result_error:
                (self.findChild(QtWidgets.QLabel, name='result_output')).setText('Ok')
            elif data.result_error_required_url:
                (self.findChild(QtWidgets.QLabel, name='result_output')).setText("Url'yi kontrol ediniz!")
            elif data.result_error_invalid_url:
                (self.findChild(QtWidgets.QLabel, name='result_output')).setText("Url'yi kontrol ediniz!")
            elif data.result_error_proxy:
                (self.findChild(QtWidgets.QLabel, name='result_output')).setText("Proxy'de sorun var!")
            elif data.result_error_timeout:
                (self.findChild(QtWidgets.QLabel, name='result_output')).setText('Timeout - Cevap dönmedi!')
            else:
                (self.findChild(QtWidgets.QLabel, name='result_output')).setText("Hata")

            if not data.result_error:
                (self.findChild(QtWidgets.QLabel, name='status_output')).setText(str(data.result_code))
                if data.result_header is not None:
                    (self.findChild(QtWidgets.QPlainTextEdit, name='headers_output')).setPlainText(str(data.result_header))
                if data.result_body is not None:
                    (self.findChild(QtWidgets.QPlainTextEdit, name='text_output')).setPlainText(str(data.result_body))
                if data.result_cookies is not None:
                    (self.findChild(QtWidgets.QPlainTextEdit, name='cookies_output')).setPlainText(str(data.result_cookies))
        except:
            self.button_func_temizle()
            (self.findChild(QtWidgets.QLabel, name='result_output')).setText('Girilen değerlerde problem var! Formata uygun giriş yapınız!')
        #
    #
    def button_func_temizle(self):
        (self.findChild(QtWidgets.QLabel, name='result_output')).setText('')
        (self.findChild(QtWidgets.QLabel, name='status_output')).setText('')
        (self.findChild(QtWidgets.QPlainTextEdit, name='headers_output')).setPlainText('')
        (self.findChild(QtWidgets.QPlainTextEdit, name='text_output')).setPlainText('')
        (self.findChild(QtWidgets.QPlainTextEdit, name='cookies_output')).setPlainText('')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
