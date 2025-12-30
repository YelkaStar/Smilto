import sys
from PyQt6.QtWidgets import QApplication
from GlobalMenu.menu_tab import MainMenu


def main():
    app = QApplication(sys.argv)
    window = MainMenu()
    window.resize(1200, 800)
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
