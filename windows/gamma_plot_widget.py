from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtGui import QPainter, QPen, QColor


class DraggablePoint:
    def __init__(self, x, y):
        self.pos = QPointF(x, y)
        self.radius = 5
        self.dragging = False

    def contains(self, point):
        return QRectF(self.pos.x() - self.radius, self.pos.y() - self.radius,
                      self.radius * 2, self.radius * 2).contains(point)

class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.points = []
        self.selected_point = None

    def setPoints(self, points):
        self.points = [DraggablePoint(p.x(), p.y()) for p in points]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()

        # Draw first quadrant axes
        print(rect.left(), rect.bottom(), rect.right(), rect.bottom())
        painter.drawLine(rect.left(), rect.bottom(), rect.right(), rect.bottom())
        painter.drawLine(rect.left(), rect.top(), rect.left(), rect.bottom())

        if not self.points:
            return

        # Draw points and lines
        pen = QPen(Qt.blue, 2)
        painter.setPen(pen)

        for point in self.points:
            painter.drawEllipse(point.pos, point.radius, point.radius)

        pen.setColor(Qt.red)
        painter.setPen(pen)

        for i in range(len(self.points) - 1):
            painter.drawLine(self.points[i].pos, self.points[i + 1].pos)

    def mousePressEvent(self, event):
        for point in self.points:
            if point.contains(event.pos()):
                self.selected_point = point
                point.dragging = True
                break

    def mouseMoveEvent(self, event):
        if self.selected_point and self.selected_point.dragging:
            # Keep x coordinate constant
            self.selected_point.pos.setY(event.pos().y())
            self.update()

    def mouseReleaseEvent(self, event):
        if self.selected_point:
            self.selected_point.dragging = False
            self.selected_point = None