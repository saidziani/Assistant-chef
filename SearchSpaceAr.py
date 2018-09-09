from PyQt5 import QtCore, QtGui, QtWidgets
import search, RecipesResAr

class SearchSpaceAr(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(800, 500)
        Form.setGeometry(300, 150, 800, 500)
        font = QtGui.QFont()
        font.setFamily("Lato")
        Form.setFont(font)
        Form.setStyleSheet("background-color: #f7f7f7;\n"
"color: #424242;")
        
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.closeWindow = Form.close

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 10, 67, 17))
        self.label_2.setObjectName("label_2")

        pixmap = QtGui.QPixmap('MonChef-logo.png').scaledToWidth(90)
        self.label_2.setPixmap(pixmap)
        self.label_2.setGeometry(QtCore.QRect(680, 15, 100, 30))

        pixmap1 = QtGui.QPixmap('retour.png').scaledToWidth(20)
        self.label.setPixmap(pixmap1)
        self.label.setGeometry(QtCore.QRect(25, 15, 20, 20))
        self.label.mousePressEvent = self.retour

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 100, 480, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFrame(False)
        # self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)

        self.lineEdit.setStyleSheet("background-color: #fff;\n"
"border-top-left-radius: 15px;border-bottom-left-radius: 15px;")
        self.lineEdit.setPlaceholderText('  مثال: طبق الارز بالدجاج..')


        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(175, 180, 500, 30))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(175, 300, 500, 30))
        self.label_4.setObjectName("label_4")

        self.checkBox_1 = QtWidgets.QCheckBox(Form)
        self.checkBox_1.setGeometry(QtCore.QRect(225, 220, 150, 30))
        self.checkBox_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(375, 220, 150, 30))
        self.checkBox_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(525, 220, 150, 30))
        self.checkBox_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(245, 340, 100, 30))
        self.checkBox_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Form)
        self.checkBox_5.setGeometry(QtCore.QRect(355, 340, 100, 30))
        self.checkBox_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Form)
        self.checkBox_6.setGeometry(QtCore.QRect(465, 340, 100, 30))
        self.checkBox_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Form)
        self.checkBox_7.setGeometry(QtCore.QRect(575, 340, 100, 30))
        self.checkBox_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.checkBox_7.setObjectName("checkBox_7")        

        self.pushButton = QtWidgets.QPushButton(Form) 
        self.pushButton.setGeometry(QtCore.QRect(175, 400, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #2fd475;\n"
"border-radius: 15px;color:#fff;font-size:14px")
        self.pushButton.clicked.connect(self.recherche)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("background-color: #fff;\n"
"border-top-right-radius: 15px;border-bottom-right-radius: 15px;")
        pixmap2 = QtGui.QPixmap('search.png').scaledToWidth(18)
        self.label_5.setPixmap(pixmap2)
        self.label_5.setGeometry(QtCore.QRect(650, 100, 30, 30))

        self.label_3.setStyleSheet("font-weight:500;\n"
"font-size:17px")
        self.label_4.setStyleSheet("font-weight:500;\n"
"font-size:17px")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MonChef. | Fr"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "اختر المطبخ المناسب:"))
        self.label_4.setText(_translate("Form", "اختر المكونات الغير مناسبة:"))
        self.checkBox_1.setText(_translate("Form", " طبيعي"))
        self.checkBox_2.setText(_translate("Form", " نباتي"))
        self.checkBox_3.setText(_translate("Form", " مرض السكري"))
        self.checkBox_4.setText(_translate("Form", " سمك"))
        self.checkBox_5.setText(_translate("Form", " غبﻻرب"))
        self.checkBox_6.setText(_translate("Form", " بحوم"))
        self.checkBox_7.setText(_translate("Form", " حليب"))
        self.pushButton.setText(_translate("Form", "بحث"))
        self.label_5.setText(_translate("Form", ""))
        

    def retour(self, event):
        print('BACK')
        self.closeWindow()
    

    def recherche(self):
        checked = []
        if self.checkBox_1.isChecked():
            checked.append(1)
        if self.checkBox_2.isChecked():
            checked.append(2)
        if self.checkBox_3.isChecked():
            checked.append(3)
        if self.checkBox_4.isChecked():
            checked.append(4)
        if self.checkBox_5.isChecked():
            checked.append(5)
        if self.checkBox_6.isChecked():
            checked.append(6)
        if self.checkBox_7.isChecked():
            checked.append(7)

        searchObj = search.Search([], 'corpus/arCorpus.txt', 2)
        query = self.lineEdit.text()
        queryToken = searchObj.text2list(query)

        queryKeyWords = searchObj.getKeyWords(queryToken)
        checked, result  = searchObj.getResult(queryKeyWords , 2)

        self.sendData(result, checked)

    def sendData(self,  data, checked):
        self.window = QtWidgets.QMainWindow()
        self.ui = RecipesResAr.RecipesResAr()
        self.ui.setupUi(self.window, data, checked)
        self.window.show()            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SearchSpaceAr()
    ui.setupUi(Form)
    Form.move(300, 150)
    Form.show()
    sys.exit(app.exec_())

