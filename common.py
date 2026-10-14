"""Tiện ích dùng chung cho bộ slide Manim giải thích bài báo LLMEmbed."""
from manim import *
from manim_slides import Slide

# ---------- Bảng màu ----------
BG = "#0B1220"
FG = "#E5E7EB"
MUTED = "#94A3B8"
ACCENT = "#38BDF8"   # xanh cyan
GREEN = "#34D399"
ORANGE = "#FB923C"
PURPLE = "#A78BFA"
RED = "#F87171"

import os

# Đặt tên font: lấy từ biến môi trường MANIM_FONT nếu có.
# Mặc định: dùng "Arial" trên Windows, None trên Linux/macOS để Pango tự nhận diện font hệ thống.
FONT = os.getenv("MANIM_FONT", "Arial" if os.name == "nt" else None)


def T(text, size=28, color=FG, **kw):
    """Text có font mặc định thống nhất."""
    if FONT:
        kw["font"] = FONT
    return Text(text, font_size=size, color=color, **kw)


def title(text, color=ACCENT):
    t = T(text, 38, color, weight=BOLD).to_edge(UP, buff=0.4)
    line = Line(LEFT * 6.5, RIGHT * 6.5, color=MUTED, stroke_width=1.5)
    line.next_to(t, DOWN, buff=0.2)
    return VGroup(t, line)


def box(label, color=ACCENT, w=2.6, h=0.9, size=24, fill=0.15):
    rect = RoundedRectangle(corner_radius=0.15, width=w, height=h,
                            color=color, stroke_width=3)
    rect.set_fill(color, opacity=fill)
    # Canh giữa văn bản nhiều dòng
    lines = [T(l, size) for l in label.split("\n")]
    txt = VGroup(*lines).arrange(DOWN, buff=0.08)
    if txt.width > w - 0.3:
        txt.scale_to_fit_width(w - 0.3)
    txt.move_to(rect)
    return VGroup(rect, txt)


def arrow(a, b, color=MUTED, **kw):
    return Arrow(a.get_right(), b.get_left(), buff=0.08, color=color,
                 stroke_width=4, max_tip_length_to_length_ratio=0.25, **kw)


def small_arrow(start, end, color=MUTED, width=2.5):
    """Mũi tên có đầu tên nhỏ cố định, dùng cho sơ đồ dày đặc."""
    a = Arrow(start, end, buff=0.06, color=color, stroke_width=width)
    a.tip.scale(0.45)
    return a


def chain(labels, color, w=2.5, h=0.95, size=20, buff=0.55):
    """Một hàng các box nối bằng mũi tên. Trả về (boxes, arrows)."""
    boxes = VGroup(*[box(l, color, w=w, h=h, size=size) for l in labels])
    boxes.arrange(RIGHT, buff=buff)
    arrows = VGroup(*[arrow(boxes[i], boxes[i + 1]) for i in range(len(boxes) - 1)])
    return boxes, arrows


def bullets(items, size=28, width=11.5):
    rows = VGroup()
    for s in items:
        dot = Dot(radius=0.07, color=ACCENT)
        t = T(s, size)
        if t.width > width:
            t.scale_to_fit_width(width)
        rows.add(VGroup(dot, t).arrange(RIGHT, buff=0.25))
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
    return rows


# Đặt nền tối qua config để manim-slides đọc được đúng kiểu màu.
config.background_color = BG


class BaseSlide(Slide):
    """Slide nền tối; mọi scene kế thừa lớp này."""
