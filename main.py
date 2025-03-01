import sys
from os import (
    getcwd
)
from os.path import (
    join
)
from PyQt5.QtWidgets import (
    QFrame,
    QApplication
)
from PyQt5.QtCore import (
    QPropertyAnimation,
    QEasingCurve
)
from PyQt5.uic import (
    loadUi
)
from modules.setStyles import SetStyles

class WindowMain(QFrame):
    def __init__(self):
        self.widthSidebar = 220
        
        #paths
        self.path_main = getcwd()
        self.ui_path = join(self.path_main, "ui", "interfaz.ui")
        self.imgPath = join(self.path_main, "images")
        
        QFrame.__init__(self)
        loadUi(self.ui_path,self)
        
        # Setting styles
        self.StyleWindow()
        
        self.eventButtons()
    
    def StyleWindow(self):
        style = SetStyles(
            self,
            self.lateral_frame,
            self.big_frame,
            self.title_frame,
            [self.btn_side, self.btn_help],
            self.label_title,
            self.imgPath,
            [self.btn_select_folder, self.btn_scan_folder, self.btn_result_folder],
            self.resultTable
        )
        style.setMainStyle()
        style.setTitleStyle()
        style.setStyleButtons()
        style.setStyleSideFrame()
        style.setStyleBigFrame()
        style.setStyleMenuButtons()
    
    def eventButtons(self):
        self.btn_side.clicked.connect(self.moveSideFrame)
    
    def moveSideFrame(self):
        width = self.lateral_frame.width()
        extend = self.widthSidebar if width == 0 else 0
        self.animationSideFrame = QPropertyAnimation(self.lateral_frame,b"minimumWidth")
        self.animationSideFrame.setDuration(500)
        self.animationSideFrame.setStartValue(width)
        self.animationSideFrame.setEndValue(extend)
        self.animationSideFrame.setEasingCurve(QEasingCurve.InOutQuart)
        self.animationSideFrame.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowMain()
    window.show()
    sys.exit(app.exec_())