import math
from PySide6.QtWidgets import QGraphicsView, QGraphicsPixmapItem
from PySide6.QtGui import QColor, QImage, QPixmap, QPainter
from PySide6.QtCore import Qt, QPoint

class CMaskLayer:
    def __init__(self, host: QGraphicsView):
        self._host = host

        self.mode_mask = 0              # bật/tắt vẽ mask
        self.brush_radius = 10          # 1..100
        self._mask_painting = False

        self._mask_img = None           # QImage Format_Alpha8, value 0..255
        self._mask_item = None          # QGraphicsPixmapItem overlay
        self._mask_color = QColor(255, 0, 0)  # màu overlay (tuỳ)

    def initMask(self, w: int, h: int):
        if self._host == None: return

        self._mask_img = QImage(w, h, QImage.Format.Format_Alpha8)
        self._mask_img.fill(0)

        if self._mask_item is None:
            self._mask_item = QGraphicsPixmapItem()
            self._mask_item.setZValue(999)  # luôn nằm trên ảnh
            self._host.scene().addItem(self._mask_item)

        self._updateMaskOverlay()

    def _updateMaskOverlay(self):
        if self._mask_img is None or self._mask_item is None:
            return

        rgba = QImage(self._mask_img.size(), QImage.Format.Format_ARGB32)
        rgba.fill(QColor(self._mask_color.red(), self._mask_color.green(), self._mask_color.blue(), 255))

        painter = QPainter(rgba)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_DestinationIn)
        painter.drawImage(0, 0, self._mask_img)   # dùng mask làm alpha
        painter.end()

        self._mask_item.setPixmap(QPixmap.fromImage(rgba))     

    def _paintMaskAt(self, x: int, y: int):
        if self._mask_img is None:
            return

        r = int(self.brush_radius)
        r = max(1, min(10, r))

        w = self._mask_img.width()
        h = self._mask_img.height()

        x0 = int(max(0, x - r))
        x1 = int(min(w - 1, x + r))
        y0 = int(max(0, y - r))
        y1 = int(min(h - 1, y + r))

        bpl = self._mask_img.bytesPerLine()   # quan trọng: có thể != w
        buf = self._mask_img.bits()           # PySide6: memoryview đã có size

        r2 = r * r

        for yy in range(y0, y1 + 1):
            dy = yy - y
            row = yy * bpl
            for xx in range(x0, x1 + 1):
                dx = xx - x
                d2 = dx*dx + dy*dy
                if d2 > r2:
                    continue

                # gradient: tâm 255, ra rìa mờ dần
                t = 1.0 - (math.sqrt(d2) / r)   # 1 -> 0
                strength = self.mode_mask / 100.0
                if strength <= 0:
                    continue

                if strength > 1.0:
                    strength = 1.0

                val = int(255 * (t * t) * strength)
                idx = row + xx
                cur = buf[idx]

                newv = cur + val
                if self.mode_mask > 0:
                    buf[idx] = 255 if newv > 255 else newv
                else:
                    buf[idx] = 0 if newv < 0 else newv
                    
    def mousePressEvent(self, event, scene_pos: QPoint) -> bool:
        # ---- MASK mode: chuột trái để vẽ mask ----
        if self.mode_mask != 0 and event.button() == Qt.MouseButton.LeftButton:
            self._mask_painting = True
            self._paintMaskAt(scene_pos.x(), scene_pos.y())
            self._updateMaskOverlay()
            return True
        
    def mouseMoveEvent(self, event, scene_pos: QPoint) -> bool:
        if self.mode_mask != 0 and self._mask_painting:
            self._paintMaskAt(scene_pos.x(), scene_pos.y())
            self._updateMaskOverlay()
            return True
        
    def mouseReleaseEvent(self, event) -> bool:
        if self.mode_mask != 0 and event.button() == Qt.MouseButton.LeftButton:
            self._mask_painting = False
            return True