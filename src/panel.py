import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculate import *
from squeeze_panel.Ui_form import *


class dash_board(QMainWindow, Ui_base_Widget):
    def __init__(self, parent=None):
        super(dash_board, self).__init__(parent)
        self.controller = controller()  # * 导入数据分析模块
        self.setupUi(self)
        self.my_init()
        self.make_data_pushButton.clicked.connect(self.make_data)

    def make_data(self):
        self.controller.default_run()

    def my_init(self):
        csvFiles = os.listdir("../data/tempData")
        csvFiles.sort()
        for csvFile in csvFiles:
            if csvFile.endswith("_words_freq.csv"):
                self.words_comboBox.addItem(csvFile)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    myWin = dash_board()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
