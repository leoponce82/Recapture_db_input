# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recaptura.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataWindow(object):
    def setupUi(self, DataWindow):
        DataWindow.setObjectName("DataWindow")
        DataWindow.resize(685, 538)
        self.centralwidget = QtWidgets.QWidget(DataWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 450, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(140, 20, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 299, 412))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_country = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_country.setReadOnly(True)
        self.lineEdit_country.setObjectName("lineEdit_country")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_country)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_province = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_province.setObjectName("comboBox_province")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_province)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_county = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_county.setObjectName("comboBox_county")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_county)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_location = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_location.setObjectName("comboBox_location")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_location)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_latt = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_latt.setText("")
        self.lineEdit_latt.setObjectName("lineEdit_latt")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_latt)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_long = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_long.setText("")
        self.lineEdit_long.setObjectName("lineEdit_long")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_long)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_altitude = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_altitude.setText("")
        self.lineEdit_altitude.setObjectName("lineEdit_altitude")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_altitude)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox_code = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_code.setObjectName("comboBox_code")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comboBox_code)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.comboBox_method = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_method.setObjectName("comboBox_method")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox_method)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_installation = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_installation.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEdit_installation.setObjectName("lineEdit_installation")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_installation)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_release = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_release.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEdit_release.setObjectName("lineEdit_release")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_release)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_release_time = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_release_time.setInputMethodHints(QtCore.Qt.ImhTime)
        self.lineEdit_release_time.setObjectName("lineEdit_release_time")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_release_time)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_collection = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_collection.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEdit_collection.setObjectName("lineEdit_collection")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.lineEdit_collection)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_collection_time = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_collection_time.setInputMethodHints(QtCore.Qt.ImhTime)
        self.lineEdit_collection_time.setObjectName("lineEdit_collection_time")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.lineEdit_collection_time)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_temp = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_temp.setObjectName("lineEdit_temp")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.lineEdit_temp)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_humi = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_humi.setObjectName("lineEdit_humi")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.lineEdit_humi)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 70, 291, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.comboBox_species = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_species.setObjectName("comboBox_species")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_species)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.comboBox_color = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_color.setObjectName("comboBox_color")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.comboBox_color.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_color)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.comboBox_sex = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_sex.setObjectName("comboBox_sex")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_sex)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.lineEdit_quantity = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_quantity.setInputMethodHints(QtCore.Qt.ImhDate)
        self.lineEdit_quantity.setObjectName("lineEdit_quantity")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_quantity)
        self.pushButton_save_quantity = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_save_quantity.setObjectName("pushButton_save_quantity")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.pushButton_save_quantity)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.textEdit_summary = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_summary.setEnabled(True)
        self.textEdit_summary.setGeometry(QtCore.QRect(360, 360, 291, 81))
        self.textEdit_summary.setReadOnly(True)
        self.textEdit_summary.setObjectName("textEdit_summary")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(360, 330, 161, 33))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        DataWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        DataWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataWindow)
        self.statusbar.setObjectName("statusbar")
        DataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataWindow)
        QtCore.QMetaObject.connectSlotsByName(DataWindow)

    def retranslateUi(self, DataWindow):
        _translate = QtCore.QCoreApplication.translate
        DataWindow.setWindowTitle(_translate("DataWindow", "DataWindow"))
        self.pushButton.setText(_translate("DataWindow", "Insertar"))
        self.label_21.setText(_translate("DataWindow", "Ingreso de datos para RECAPTURA"))
        self.label.setText(_translate("DataWindow", "País:"))
        self.lineEdit_country.setText(_translate("DataWindow", "Ecuador"))
        self.label_2.setText(_translate("DataWindow", "Provincia:"))
        self.label_3.setText(_translate("DataWindow", "Cantón:"))
        self.label_4.setText(_translate("DataWindow", "Localidad:"))
        self.label_5.setText(_translate("DataWindow", "Latitud:"))
        self.label_6.setText(_translate("DataWindow", "Longitud:"))
        self.label_7.setText(_translate("DataWindow", "Altitud:"))
        self.label_8.setText(_translate("DataWindow", "Codigo de trampa:"))
        self.label_9.setText(_translate("DataWindow", "Método de trampa:"))
        self.label_10.setText(_translate("DataWindow", "Fecha de instalación:"))
        self.label_11.setText(_translate("DataWindow", "Fecha de liberación:"))
        self.label_12.setText(_translate("DataWindow", "Hora de liberación:"))
        self.label_13.setText(_translate("DataWindow", "Fecha de colecta:"))
        self.label_14.setText(_translate("DataWindow", "Hora de colecta:"))
        self.label_15.setText(_translate("DataWindow", "Temperatura:"))
        self.label_16.setText(_translate("DataWindow", "Humedad:"))
        self.label_17.setText(_translate("DataWindow", "Especie:"))
        self.label_18.setText(_translate("DataWindow", "Color de pigmento:"))
        self.comboBox_color.setItemText(0, _translate("DataWindow", "amarillo"))
        self.comboBox_color.setItemText(1, _translate("DataWindow", "rosado"))
        self.comboBox_color.setItemText(2, _translate("DataWindow", "no color"))
        self.label_19.setText(_translate("DataWindow", "Sexo:"))
        self.comboBox_sex.setItemText(0, _translate("DataWindow", "macho"))
        self.comboBox_sex.setItemText(1, _translate("DataWindow", "hembra"))
        self.label_22.setText(_translate("DataWindow", "Cantidad:"))
        self.pushButton_save_quantity.setText(_translate("DataWindow", "Guardar"))
        self.label_20.setText(_translate("DataWindow", "Observaciones:"))
        self.label_23.setText(_translate("DataWindow", "Valores guardados:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DataWindow = QtWidgets.QMainWindow()
    ui = Ui_DataWindow()
    ui.setupUi(DataWindow)
    DataWindow.show()
    sys.exit(app.exec_())
