"""Phần 2: So sánh hai mô hình tư duy – prompt-based vs LLMEmbed."""
from common import *


class S02Paradigm(BaseSlide):
    def construct(self):
        ttl = title("Hai cách dùng LLM cho phân loại văn bản")
        self.play(FadeIn(ttl))

        # ---- Hàng A: prompt-based ----
        lab_a = T("Prompt-based paradigm", 26, RED, weight=BOLD)
        boxes_a, arrows_a = chain(
            ["Văn bản", "Prompt\n(clue + reasoning)", "LLM lớn\n(sinh văn bản)",
             "Phân tích câu trả lời\n→ nhãn"], RED)
        row_a = VGroup(boxes_a, arrows_a)
        grp_a = VGroup(lab_a, row_a).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        grp_a.move_to(UP * 1.3)

        self.play(FadeIn(lab_a))
        for i, b in enumerate(boxes_a):
            anims = [FadeIn(b, shift=RIGHT * 0.2)]
            if i > 0:
                anims.append(GrowArrow(arrows_a[i - 1]))
            self.play(*anims, run_time=0.5)
        note_a = T("Chậm, tốn kém; mỗi mẫu cần một prompt riêng", 22, MUTED)
        note_a.next_to(grp_a, DOWN, buff=0.2)
        self.play(FadeIn(note_a))
        self.next_slide()

        # ---- Hàng B: LLMEmbed ----
        lab_b = T("LLMEmbed paradigm", 26, GREEN, weight=BOLD)
        boxes_b, arrows_b = chain(
            ["Văn bản", "LLM nhỏ\n(đóng băng)", "Embedding\nđa tầng, đa mô hình",
             "Classifier nhẹ\n→ nhãn"], GREEN)
        row_b = VGroup(boxes_b, arrows_b)
        grp_b = VGroup(lab_b, row_b).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        grp_b.move_to(DOWN * 1.6)

        self.play(FadeIn(lab_b))
        for i, b in enumerate(boxes_b):
            anims = [FadeIn(b, shift=RIGHT * 0.2)]
            if i > 0:
                anims.append(GrowArrow(arrows_b[i - 1]))
            self.play(*anims, run_time=0.5)
        note_b = T("Ánh xạ trực tiếp văn bản → nhãn; chạy batch song song", 22, MUTED)
        note_b.next_to(grp_b, DOWN, buff=0.2)
        self.play(FadeIn(note_b))
        self.next_slide()

        # ---- Nhấn mạnh sự khác biệt ----
        self.play(boxes_a[2].animate.set_opacity(0.35),
                  Indicate(boxes_b[1], color=GREEN, scale_factor=1.12))
        punch = T("Không dùng khả năng SINH của LLM – chỉ dùng khả năng BIỂU DIỄN",
                  26, ORANGE, weight=BOLD)
        punch.to_edge(DOWN, buff=0.25)
        self.play(FadeIn(punch, shift=UP * 0.2))
        self.next_slide()
