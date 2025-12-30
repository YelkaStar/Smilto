from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor, QImage
from PyQt6.QtCore import Qt


class Pen1:
    def draw_point(self, canvas: QImage, x: int, y: int) -> None:
        painter = QPainter(canvas)
        pen = QPen(QColor(255, 0, 0), 15)
        painter.setPen(pen)
        painter.drawPoint(x, y)
        painter.end()


class CanvasWidget(QWidget):
    def __init__(self, w=1000, h=700):
        super().__init__()
        self.canvas = QImage(w, h, QImage.Format.Format_ARGB32)
        self.canvas.fill(Qt.GlobalColor.white)
        self.tool = Pen1()
        self.setMinimumSize(w, h)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            pos = event.position()
            x, y = int(pos.x()), int(pos.y())
            self.tool.draw_point(self.canvas, x, y)
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            pos = event.position()
            x, y = int(pos.x()), int(pos.y())
            self.tool.draw_point(self.canvas, x, y)
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.canvas)
        painter.end()
