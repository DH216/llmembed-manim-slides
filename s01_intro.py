"""Phần 1: Tiêu đề, nội dung trình bày và động cơ nghiên cứu."""
from common import *


class S01Title(BaseSlide):
    def construct(self):
        name = T("LLMEmbed", 84, ACCENT, weight=BOLD)
        sub = T("Rethinking Lightweight LLM's Genuine Function\nin Text Classification", 34)
        meta = T("Chun Liu, Hongguang Zhang, Kainan Zhao, Xinghai Ju, Lin Yang  ·  ACL 2024",
                 22, MUTED)
        g = VGroup(name, sub, meta).arrange(DOWN, buff=0.5)
        self.play(Write(name))
        self.play(FadeIn(sub, shift=UP * 0.3), FadeIn(meta))
        self.next_slide()

        self.play(FadeOut(g))
        ttl = title("Nội dung trình bày")
        agenda = bullets([
            "1. Động cơ: vì sao prompt + LLM lớn là chưa đủ?",
            "2. Ý tưởng: dùng LLM nhỏ làm bộ trích xuất embedding",
            "3. Kiến trúc LLMEmbed: trích xuất đa tầng, hợp nhất, phân loại",
            "4. Công thức chính",
            "5. Kết quả hiệu quả & kết luận",
        ], size=30)
        self.play(FadeIn(ttl))
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in agenda],
                              lag_ratio=0.25))
        self.next_slide()


class S01Problem(BaseSlide):
    def construct(self):
        ttl = title("Động cơ: prompt-learning + LLM lớn rất tốn kém")
        self.play(FadeIn(ttl))

        items = [
            "Prompt-learning (vd. CARP trên GPT-3) đạt SOTA trên 5 benchmark phân loại",
            "Nhưng phụ thuộc LLM rất lớn → tốn tham số, điện năng, thời gian suy luận",
            "LLM nhỏ: khả năng suy luận/emergent yếu hơn → prompt kém hiệu quả",
            "LLM là mô hình sinh → vẫn thua mô hình phân biệt ở phân loại văn bản",
        ]
        rows = bullets(items, size=28).next_to(ttl, DOWN, buff=0.7)
        rows.to_edge(LEFT, buff=0.8)
        for r in rows:
            self.play(FadeIn(r, shift=RIGHT * 0.3))
            self.next_slide()

        q = box("LLM nhỏ thực sự giỏi điều gì?\n→ Biểu diễn ngữ nghĩa (embedding)",
                ORANGE, w=9.5, h=1.3, size=30, fill=0.25)
        q.to_edge(DOWN, buff=0.6)
        self.play(GrowFromCenter(q))
        self.next_slide()
