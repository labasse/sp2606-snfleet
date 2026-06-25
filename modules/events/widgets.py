"""Custom widgets for the SkyNetFleet application."""
from pathlib import Path
from typing import override

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QColor, QPainter, QPixmap, QResizeEvent
from PySide6.QtWidgets import (
    QGraphicsItem,
    QGraphicsScene,
    QGraphicsView,
    QSizePolicy,
    QWidget,
)

ASSETS_PATH = Path(__file__).parent / "ui"
MOTOR_POSITIONS = {
    "neck_pitch"    : (195, 118),
    "shoulder_left" : (115, 166),
    "shoulder_right": (277, 166),
    "elbow_left"    : (103, 282),
    "elbow_right"   : (286, 282),
    "torso_yaw"     : (195, 330),
    "hip_left"      : (128, 381),
    "hip_right"     : (261, 381),
    "knee_left"     : (140, 532),
    "knee_right"    : (248, 532),
    "ankle_left"    : (142, 667),
    "ankle_right"   : (247, 667),
}

RADIUS = 20
MARKER_ALPHA = 128

class BotMapWidget(QGraphicsView):
    """Custom widget to display robot positions on a map."""

    _items: list[QGraphicsItem]
    _steps: list[(float,QColor)]

    def __init__(self, parent: QWidget | None = None) -> None:
        """Initialize the map widget."""
        super().__init__(parent)
        self._items = []
        self._steps = [
            (0.0, QColor(Qt.GlobalColor.darkGray)),
            (40.0, QColor(Qt.GlobalColor.green)),
            (60.0, QColor(Qt.GlobalColor.yellow)),
            (float("inf"), QColor(Qt.GlobalColor.red)),
        ]
        for _, color in self._steps:
            color.setAlpha(MARKER_ALPHA)  # Semi-transparent
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.curImg = QPixmap(ASSETS_PATH / "00.png")
        self.ratio = self.curImg.width() / self.curImg.height()
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(self.curImg.rect())
        self.scene.addPixmap(self.curImg).setTransformationMode(Qt.SmoothTransformation)
        self.setScene(self.scene)

    @override
    def resizeEvent(self, event: QResizeEvent) -> None:
        """Handle resizing to keep the map fitting the view."""
        new_height = event.size().height()
        new_width = int(new_height * self.ratio)
        self.setFixedWidth(new_width)
        super().resizeEvent(QResizeEvent(QSize(new_width, new_height), event.oldSize()))
        if hasattr(self, "scene") and self.scene:
            self.fitInView(self.scene.sceneRect())

    def set_temps(self, temps: dict[str, float]) -> None:
        """Update the map with motor temperatures."""
        for item in self._items:
            self.scene.removeItem(item)
        self._items.clear()
        for motor_id, temp in temps.items():
            if motor_id in MOTOR_POSITIONS:
                x, y = MOTOR_POSITIONS[motor_id]
                item = self.scene.addEllipse(
                    x - RADIUS, y - RADIUS, 2 * RADIUS, 2 * RADIUS,
                    brush=self._temp_to_color(temp))
                item.setToolTip(f"{motor_id}: {temp:.1f} °C")
                self._items.append(item)

    def _temp_to_color(self, temp: float) -> Qt.GlobalColor:
        """Convert temperature to a color for visualization."""
        for threshold, color in self._steps:
            if temp < threshold:
                return color
        return self._steps[-1][1]
