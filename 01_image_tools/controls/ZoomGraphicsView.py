from PySide6.QtWidgets import QGraphicsView, QGraphicsRectItem
from PySide6.QtCore import Qt, Signal, QRectF, QPointF
from PySide6.QtGui import QPainter, QPen

class ZoomGraphicsView(QGraphicsView):
    mousePosChanged = Signal(int, int)
    roiSelected = Signal(int, int, int, int)  # x, y, w, h

    def __init__(self, parent=None):
        super().__init__(parent)

        # ----- zoom -----
        self._zoom = 0
        self._zoom_step = 1.15
        self._zoom_min = -10
        self._zoom_max = 20

        self.setTransformationAnchor(
            QGraphicsView.ViewportAnchor.AnchorUnderMouse
        )
        self.setResizeAnchor(
            QGraphicsView.ViewportAnchor.AnchorUnderMouse
        )

        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        self.setCursor(Qt.CursorShape.ArrowCursor)
        self.setMouseTracking(True)

        self.setRenderHint(
            QPainter.RenderHint.SmoothPixmapTransform, True
        )

        # ----- pan -----
        self._panning = False
        self._pan_start = None

        # ----- ROI -----
        self._roi_start = None
        self._roi_item = None
        self._drawing_roi = False

    # ================= ZOOM =================
    def wheelEvent(self, event):
        if event.angleDelta().y() == 0:
            return

        zoom_in = event.angleDelta().y() > 0
        if zoom_in and self._zoom >= self._zoom_max:
            return
        if not zoom_in and self._zoom <= self._zoom_min:
            return

        factor = self._zoom_step if zoom_in else 1 / self._zoom_step
        self.scale(factor, factor)
        self._zoom += 1 if zoom_in else -1

    # ================= MOUSE =================
    def mousePressEvent(self, event):
        scene_pos = self.mapToScene(event.position().toPoint())

        # ---- vẽ ROI (chuột phải) ----
        if event.button() == Qt.MouseButton.RightButton:
            self._drawing_roi = True
            self._roi_start = scene_pos

            if self._roi_item:
                self.scene().removeItem(self._roi_item)

            pen = QPen(Qt.GlobalColor.green)
            pen.setWidth(2)
            pen.setCosmetic(True)

            self._roi_item = QGraphicsRectItem()
            self._roi_item.setPen(pen)
            self.scene().addItem(self._roi_item)
            return

        # ---- pan (chuột trái) ----
        if event.button() == Qt.MouseButton.LeftButton:
            self._panning = True
            self._pan_start = event.position().toPoint()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        scene_pos = self.mapToScene(event.position().toPoint())

        # ---- phát tọa độ pixel ----
        self.mousePosChanged.emit(int(scene_pos.x()), int(scene_pos.y()))

        # ---- vẽ ROI ----
        if self._drawing_roi and self._roi_start:
            rect = QRectF(self._roi_start, scene_pos).normalized()
            self._roi_item.setRect(rect)

        # ---- pan ----
        if self._panning:
            delta = event.position().toPoint() - self._pan_start
            self._pan_start = event.position().toPoint()
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        # ---- kết thúc ROI ----
        if event.button() == Qt.MouseButton.RightButton and self._drawing_roi:
            self._drawing_roi = False

            rect = self._roi_item.rect().toRect()
            if rect.width() > 5 and rect.height() > 5:
                self.roiSelected.emit(
                    rect.x(), rect.y(), rect.width(), rect.height()
                )

        # ---- kết thúc pan ----
        if event.button() == Qt.MouseButton.LeftButton:
            self._panning = False
            self.setCursor(Qt.CursorShape.ArrowCursor)

        super().mouseReleaseEvent(event)

    # ================= RESET =================
    def resetZoom(self, item=None):
        self.resetTransform()
        self._zoom = 0
        if item:
            self.fitInView(item, Qt.AspectRatioMode.KeepAspectRatio)
