import cv2
import numpy as np
from PySide6.QtGui import QImage, QPixmap, QIcon, QPainter
from PySide6.QtCore import Qt

def thumbnail_from_numpy(img_bgr: np.ndarray, size=64) -> QIcon:
    """
    img_bgr: numpy image (H, W, 3) BGR
    return: QIcon thumbnail size x size
    """

    if img_bgr is None or img_bgr.size == 0:
        return QIcon()

    h, w = img_bgr.shape[:2]

    # scale giữ aspect ratio
    scale = size / max(w, h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    thumb_bgr = cv2.resize(
        img_bgr, (new_w, new_h),
        interpolation=cv2.INTER_AREA
    )

    # BGR → RGB
    thumb_rgb = cv2.cvtColor(thumb_bgr, cv2.COLOR_BGR2RGB)

    # QImage zero-copy
    h, w, ch = thumb_rgb.shape
    bytes_per_line = ch * w

    qimg = QImage(
        thumb_rgb.data,
        w,
        h,
        bytes_per_line,
        QImage.Format.Format_RGB888
    )

    # pad vào canvas 64x64 để icon không bị lệch
    canvas = QPixmap(size, size)
    canvas.fill(Qt.GlobalColor.transparent)

    pix = QPixmap.fromImage(qimg)
    painter = QPainter(canvas)
    x = (size - w) // 2
    y = (size - h) // 2
    painter.drawPixmap(x, y, pix)
    painter.end()

    return QIcon(canvas)