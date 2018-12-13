#!/usr/bin/env python3
import sys
import pandas as pd
import catboost
import lightgbm as lgb
from PyQt5.QtWidgets import QApplication, qApp, QMainWindow, QWidget
from PyQt5.QtCore import QObject, pyqtSignal, QThread, QTimer
from widget import Ui_Widget


class AbstractModel(QObject):
    status = pyqtSignal(str)
    thread_id = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.thread = QThread()
        self.moveToThread(self.thread)
        qApp.aboutToQuit.connect(self.thread.quit)
        self.thread.start()

    def run(self):
        self.status.emit('In progress')
        self.thread_id.emit(str(int(QThread.currentThreadId())))
        self.predict()
        self.status.emit('Done')

    def predict(self):
        raise NotImplementedError()


class CatBoostModel(AbstractModel):
    def __init__(self):
        super().__init__()
        self.model = catboost.CatBoostClassifier()
        self.model.load_model('./catboost_model.bin')
        self.X_test = pd.read_csv('./amazon/test.csv').drop('id', axis=1)

    def predict(self):
        for _ in range(10):
            self.model.predict(self.X_test, thread_count=2)


class LightGBMModel(AbstractModel):
    def __init__(self):
        super().__init__()
        self.model = lgb.Booster(model_file='./lightgbm_model.bin')
        self.X_test = pd.read_csv('./amazon/test.csv').drop('id', axis=1)

    def predict(self):
        for _ in range(50):
            self.model.predict(self.X_test)


class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.widget_thread_id.setText(str(int(QThread.currentThreadId())))
        self.progress = 0
        QTimer.singleShot(10, self.update_progress_bar)

    def update_progress_bar(self):
        self.progressBar.setValue(self.progress)
        self.progress += 1
        if self.progress > 100:
            self.progress = 0
        QTimer.singleShot(10, self.update_progress_bar)


class MainWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.catboost_model = CatBoostModel()
        self.lightgbm_model = LightGBMModel()
        self.widget = Widget(self)
        self.widget.run_catboost.clicked.connect(self.catboost_model.run)
        self.widget.run_lightgbm.clicked.connect(self.lightgbm_model.run)
        self.catboost_model.status.connect(self.widget.status.setText)
        self.lightgbm_model.status.connect(self.widget.status.setText)
        self.catboost_model.thread_id.connect(self.widget.model_thread_id.setText)
        self.lightgbm_model.thread_id.connect(self.widget.model_thread_id.setText)
        self.setCentralWidget(self.widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
