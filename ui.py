#pyuic5 xyz.ui > xyz.py 
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640,480)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)
        #test
        self.image_label1 = QtWidgets.QLabel(Form)
        self.image_label1.setObjectName("image_label1")
   

        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setObjectName("control_bt")

        self.verticalLayout.addWidget(self.control_bt)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Barcode Scanner"))
        self.image_label.setText(_translate("Form", ""))
        self.image_label1.setText(_translate("Form", ""))
        self.control_bt.setText(_translate("Form", "Start"))
