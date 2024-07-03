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
    def __init__(self, x_range=(0, 255), y_range=(0, 255), parent=None):
        super().__init__(parent)
        self.points = []
        self.selected_point = None
        self.x_range = x_range
        self.y_range = y_range

    def setPoints(self, points):
        self.points = [DraggablePoint(p.x(), p.y()) for p in points]
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect()

        # Draw first quadrant axes
        painter.drawLine(rect.left(), rect.bottom(), rect.right(), rect.bottom())
        painter.drawLine(rect.left(), rect.top(), rect.left(), rect.bottom())
        self.drawAxisLabels(painter, rect)

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

    def drawAxisLabels(self, painter, rect):
        # Set font for axis labels
        font = painter.font()
        font.setPointSize(8)
        painter.setFont(font)

        # Draw X axis labels
        x_interval = (self.x_range[1] - self.x_range[0]) // 15  # clac count
        for i in range(self.x_range[0], self.x_range[1], x_interval):
            x = rect.left() + (i - self.x_range[0]) * rect.width() / (
                    self.x_range[1] - self.x_range[0])  # Calculate the position of each point on the canvas
            painter.drawText(x - 10, rect.bottom() - 5, str(i))

        # Ensure the last label on the X axis is drawn
        painter.drawText(rect.right() - 15, rect.bottom() - 5, str(self.x_range[1]))

        # Draw Y axis labels
        y_interval = (self.y_range[1] - self.y_range[0]) // 15
        for i in range(self.y_range[0], self.y_range[1], y_interval):
            y = rect.bottom() - (i - self.y_range[0]) * rect.height() / (self.y_range[1] - self.y_range[0])
            painter.drawText(rect.left() + 5, y + 5, str(i))

        # Ensure the last label on the Y axis is drawn
        painter.drawText(rect.left() + 5, rect.top() + 10, str(self.y_range[1]))

    def mousePressEvent(self, event):
        for point in self.points:
            if point.contains(event.pos()):
                self.selected_point = point
                point.dragging = True
                break

    def mouseMoveEvent(self, event):
        if self.selected_point and self.selected_point.dragging:
            rect = self.rect()
            new_y = max(rect.top(), min(event.pos().y(), rect.bottom()))
            self.selected_point.pos.setY(new_y)  # Limit the range of y-coordinate movement
            self.update()

    def mouseReleaseEvent(self, event):
        if self.selected_point:
            self.selected_point.dragging = False
            self.selected_point = None

    def getRealPoints(self):
        rect = self.rect()
        plot_points = []
        for point in self.points:
            y_ratio = (rect.bottom() - point.pos.y()) / rect.height()
            real_y = int(self.y_range[0] + y_ratio * (self.y_range[1] - self.y_range[0]))
            plot_points.append(real_y)
        return plot_points
