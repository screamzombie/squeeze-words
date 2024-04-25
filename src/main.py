from panel import *
from calculate import *

if __name__ == '__main__':
    c = controller()
    c.default_run()
    app = QApplication(sys.argv)  
    myWin = windows()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())

