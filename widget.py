# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(400, 292)
        self.verticalLayout = QtWidgets.QVBoxLayout(Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.run_lightgbm = QtWidgets.QPushButton(Widget)
        self.run_lightgbm.setObjectName("run_lightgbm")
        self.verticalLayout.addWidget(self.run_lightgbm)
        self.run_catboost = QtWidgets.QPushButton(Widget)
        self.run_catboost.setObjectName("run_catboost")
        self.verticalLayout.addWidget(self.run_catboost)
        self.run_catboost_pool = QtWidgets.QPushButton(Widget)
        self.run_catboost_pool.setObjectName("run_catboost_pool")
        self.verticalLayout.addWidget(self.run_catboost_pool)
        self.run_catboost_features_data = QtWidgets.QPushButton(Widget)
        self.run_catboost_features_data.setObjectName("run_catboost_features_data")
        self.verticalLayout.addWidget(self.run_catboost_features_data)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.widget_thread_id = QtWidgets.QLineEdit(Widget)
        self.widget_thread_id.setObjectName("widget_thread_id")
        self.horizontalLayout.addWidget(self.widget_thread_id)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.model_thread_id = QtWidgets.QLineEdit(Widget)
        self.model_thread_id.setObjectName("model_thread_id")
        self.horizontalLayout_2.addWidget(self.model_thread_id)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.status = QtWidgets.QLineEdit(Widget)
        self.status.setObjectName("status")
        self.horizontalLayout_3.addWidget(self.status)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.progressBar = QtWidgets.QProgressBar(Widget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.run_lightgbm.setText(_translate("Widget", "Run LightGBM (X is Pandas df)"))
        self.run_catboost.setText(_translate("Widget", "Run CatBoost (X is Pandas df)"))
        self.run_catboost_pool.setText(_translate("Widget", "Run CatBoost (X is Pool)"))
        self.run_catboost_features_data.setText(_translate("Widget", "Run CatBoost (X is Pool with FeaturesData)"))
        self.label.setText(_translate("Widget", "WidgetThread Id"))
        self.label_2.setText(_translate("Widget", "Model Thread Id"))
        self.label_3.setText(_translate("Widget", "Status"))

