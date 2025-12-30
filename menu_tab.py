from PyQt6.QtWidgets import QWidget, QPushButton, QTabWidget
from Window.work_area import CanvasWidget


class MainMenu(QTabWidget):
    def __init__(self):
        super().__init__()

        self.GlobalMenu = QWidget()
        self.addTab(self.GlobalMenu, "Главная")

        self.CreateWindow = QPushButton("Создание Окна", self.GlobalMenu)
        self.CreateWindow.setFixedSize(160, 50)
        self.CreateWindow.move(50, 50)
        self.CreateWindow.clicked.connect(self.NewWindow)

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.CloseWindow)

    def NewWindow(self):
        page = CanvasWidget(10000, 10000)
        self.addTab(page, "Холст")
        self.setCurrentWidget(page)

    def CloseWindow(self, index):
        if index != 0:
            self.removeTab(index)
