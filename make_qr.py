# -*- coding: utf-8 -*-
"""작게 표시해도 잘 인식되는 단순 QR 코드 — 칸 수 최소화"""
import qrcode
import qrcode.image.svg
from qrcode.constants import ERROR_CORRECT_L
import os

URL = "https://socialbiz1.github.io/wedding/"
OUT_DIR = r"C:\Users\NHN\wedding_intro\qr"
os.makedirs(OUT_DIR, exist_ok=True)

def make(url):
    # ERROR_CORRECT_L (7%) = 칸 수 최소 → 칸 하나가 커져서 작게 봐도 인식 잘 됨
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_L,
        box_size=60,   # 칸당 60px → 고해상도
        border=4,      # 표준 여백(quiet zone)
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr

qr = make(URL)
modules = qr.modules_count  # 한 변의 칸 수
print(f"URL: {URL}")
print(f"버전: {qr.version}  /  칸 수: {modules} x {modules}  (작을수록 단순=인식 쉬움)")

# 1) PNG 고해상도 흑백
img = qr.make_image(fill_color="black", back_color="white")
img.save(os.path.join(OUT_DIR, "qr_simple.png"))
print(f"  qr_simple.png  ({img.size[0]}x{img.size[1]}px)")

# 2) 벡터 SVG (인쇄소용 — 무한 확대)
qr_svg = make(URL)
svg = qr_svg.make_image(image_factory=qrcode.image.svg.SvgPathImage)
svg.save(os.path.join(OUT_DIR, "qr_simple.svg"))
print("  qr_simple.svg  (vector)")
