from PyQt5.QtGui import (
    QIcon,
    QPixmap
)
from PyQt5.QtCore import (
    QSize,
    Qt,
    QPropertyAnimation
)
from PyQt5.QtWidgets import (
    QGraphicsDropShadowEffect,
    QFileDialog
)
from os.path import (
    join
)
from modules.zizefolder import scan_and_sort_folders


class SetStyles:
    def __init__(self, mainFrame, sideFrame, big_frame, titleFrame,buttons, label_title, pathImages, menuButtons):
        self.imagePath = pathImages
        self.mainFrame = mainFrame
        self.sideFrame = sideFrame
        self.bigFrame = big_frame
        self.titleFrame = titleFrame
        self.buttons = buttons
        self.labelTitle = label_title
        self.menuButtons = menuButtons
        
        self.menuButtons[0].enterEvent = self.hoverInButton
        self.menuButtons[0].leaveEvent = self.hoverOutButton
        self.menuButtons[0].clicked.connect(self.openFolder)
        
        self.menuButtons[1].enterEvent = self.hoverInButton1
        self.menuButtons[1].leaveEvent = self.hoverOutButton1
        
        self.menuButtons[2].enterEvent = self.hoverInButton2
        self.menuButtons[2].leaveEvent = self.hoverOutButton2
        
        self.Images()
        
    def Images(self):
        self.imageMenu = QPixmap(join(self.imagePath, "btn_menu.png"))
        self.iconMenu = QIcon(self.imageMenu)
        
        self.imageFolder = QPixmap(join(self.imagePath, "btn_open_folder.png"))
        self.imageScan = QPixmap(join(self.imagePath, "btn_search.png"))
        self.imageResult = QPixmap(join(self.imagePath, "btn_result.png"))
        self.iconFolder = QIcon(self.imageFolder)
        self.iconScan = QIcon(self.imageScan)
        self.iconResult = QIcon(self.imageResult)
        
        self.iconsBtnMenu = [self.iconFolder, self.iconScan, self.iconResult]
    
    def setMainStyle(self):
        style = """
            background-color: #2a2b2b;
        """
        self.mainFrame.setStyleSheet(style)
        
    def setTitleStyle(self):
        style = """
            color: white;
            font-size: 20px;
        """
        self.labelTitle.setStyleSheet(style)
        
    def setStyleButtons(self):
        style = """
            border: none;
            border-radius: 10px;
            background-color: #5a5b5b;
        """
        for btn in self.buttons:
            btn.setStyleSheet(style)
        self.buttons[0].setIcon(self.iconMenu)
        self.buttons[0].setIconSize(QSize(30,30))
        
    def setStyleSideFrame(self):
        style = """
            background-color: #3a5b5b;
            border-radius: 10px;
        """
        self.sideFrame.setStyleSheet(style)
        
    def setStyleBigFrame(self):
        style = """
            background-color: #3b5a5a;
            border-radius: 10px;
        """
        self.bigFrame.setStyleSheet(style)
        
    def setStyleMenuButtons(self):
        
        style = """
            background-color: #f2f2f2;
            border-radius: 10px;
            font-size: 20px;
        """
        
        packShadows = []
        
        for i in range(0, len(self.menuButtons)):
            packShadows.append(QGraphicsDropShadowEffect(self.menuButtons[i]))
            packShadows[i].setYOffset(10)
            packShadows[i].setBlurRadius(10)
        
        for button in self.menuButtons:
            button.setStyleSheet(style)
            
        for i in range(0, len(self.iconsBtnMenu)):
            self.menuButtons[i].setIcon(self.iconsBtnMenu[i])
            self.menuButtons[i].setIconSize(QSize(30,30))
            self.menuButtons[i].setGraphicsEffect(packShadows[i])
            self.menuButtons[i].setFocusPolicy(Qt.StrongFocus)
            
    def animationIcons(self):
        self.animations = []
        for i in range(len(self.menuButtons)):
            self.animations.append(QPropertyAnimation(self.menuButtons[i],b'iconSize'))
            self.animations[i].setDuration(500)
            self.animations[i].setStartValue(QSize(35,35))
            self.animations[i].setEndValue(QSize(30,30))
            self.animations[i].start()
            
    def hoverInButton(self, event):
        animation = QPropertyAnimation(self.menuButtons[0],b'iconSize')
        animation.setDuration(1000)
        animation.setStartValue(QSize(35,35))
        animation.setEndValue(QSize(30,30))
        animation.start()
        
    def hoverOutButton(self, event):
        animation = QPropertyAnimation(self.menuButtons[0],b'iconSize')
        animation.setDuration(1000)
        animation.setStartValue(QSize(30,30))
        animation.setEndValue(QSize(35,35))
        animation.start()
        
    def hoverInButton1(self, event):
        animation = QPropertyAnimation(self.menuButtons[1],b'iconSize')
        animation.setDuration(1000)
        animation.setStartValue(QSize(35,35))
        animation.setEndValue(QSize(30,30))
        animation.start()
        
    def hoverOutButton1(self, event):
        animation = QPropertyAnimation(self.menuButtons[1],b'iconSize')
        animation.setDuration(1000)
        animation.setStartValue(QSize(30,30))
        animation.setEndValue(QSize(35,35))
        animation.start()
        
    def hoverInButton2(self, event):
        animation = QPropertyAnimation(self.menuButtons[2],b'iconSize')
        animation.setDuration(1000)
        animation.setStartValue(QSize(35,35))
        animation.setEndValue(QSize(30,30))
        animation.start()
        
    def hoverOutButton2(self, event):
        animation = QPropertyAnimation(self.menuButtons[2],b'iconSize')
        animation.setDuration(1000)
        animation.setStartValue(QSize(30,30))
        animation.setEndValue(QSize(35,35))
        animation.start()
        
    def openFolder(self):
        folder = QFileDialog.getExistingDirectory(self.mainFrame,"Seleccionar Carpeta", "", QFileDialog.ShowDirsOnly)

        try:
            scan_and_sort_folders(folder)
        except:
            print("ERROR")