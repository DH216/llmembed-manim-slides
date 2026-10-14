"""Phần 5: Hiệu quả tính toán và kết luận (không cần LaTeX)."""
from common import *


class S05Efficiency(BaseSlide):
    def construct(self):
        ttl = title("Hiệu quả: gần như không tốn tài nguyên")
        self.play(FadeIn(ttl))

        # Số liệu từ abstract của bài báo (so với các phương pháp đối chứng)
        metrics = [("Tham số mô hình", 4.0, ACCENT),
                   ("Điện năng tiêu thụ", 1.8, GREEN),
                   ("Thời gian chạy", 1.5, ORANGE)]
        W = 7.0
        x0 = -2.5

        base_note = T("Thanh xám = 100% (phương pháp đối chứng)", 20, MUTED)
        base_note.next_to(ttl, DOWN, buff=0.4)
        self.play(FadeIn(base_note))

        y = 1.2
        for name, pct, col in metrics:
            lab = T(name, 26).move_to([-5.2, y, 0])
            lab.set_x(-5.2 + lab.width / 2 - 0.8)
            full = Rectangle(width=W, height=0.6, stroke_width=0)
            full.set_fill(MUTED, opacity=0.25)
            full.move_to([x0 + W / 2, y, 0])
            bar = Rectangle(width=max(W * pct / 100, 0.06), height=0.6, stroke_width=0)
            bar.set_fill(col, opacity=0.95)
            bar.align_to(full, LEFT).set_y(y)
            val = T(f"{pct:g}%", 28, col, weight=BOLD).next_to(full, RIGHT, buff=0.3)

            self.play(FadeIn(lab), FadeIn(full))
            self.play(GrowFromEdge(bar, LEFT), FadeIn(val))
            self.next_slide()
            y -= 1.3

        foot = T("Không cần fine-tune LLM · so với các phương pháp dùng LLM lớn như GPT-3",
                 22, FG)
        foot.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(foot))
        self.next_slide()


class S05Takeaways(BaseSlide):
    def construct(self):
        ttl = title("Kết luận")
        self.play(FadeIn(ttl))
        rows = bullets([
            "Dùng LLM nhỏ như bộ trích xuất đặc trưng, không phải bộ sinh văn bản",
            "Trích embedding đa tầng, đa mô hình rồi hợp nhất → bền vững, phân biệt tốt",
            "LLM đóng băng; chỉ huấn luyện classifier nhẹ bằng cross-entropy",
            "Chỉ ~4% tham số, 1.8% điện năng, 1.5% thời gian so với đối chứng",
        ], size=28).next_to(ttl, DOWN, buff=0.8)
        rows.to_edge(LEFT, buff=0.8)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3))
            self.next_slide()

        code = T("Code: github.com/ChunLiu-cs/LLMEmbed-ACL2024", 24, ACCENT)
        code.to_edge(DOWN, buff=0.6)
        self.play(FadeIn(code))
        self.next_slide()
