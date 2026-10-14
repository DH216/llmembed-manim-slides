"""Phần 3: Kiến trúc LLMEmbed – trích xuất đa tầng, hợp nhất, phân loại."""
from common import *


def layer_stack(color):
    layers = VGroup(*[
        Rectangle(width=1.6, height=0.22, stroke_width=2, color=color)
        .set_fill(color, opacity=0.15)
        for _ in range(4)
    ]).arrange(DOWN, buff=0.06)
    return layers


def vec(color, n=6):
    return VGroup(*[
        Square(0.22, stroke_width=1.5, color=color).set_fill(color, opacity=0.6)
        for _ in range(n)
    ]).arrange(RIGHT, buff=0.03)


class S03Pipeline(BaseSlide):
    def construct(self):
        ttl = title("Kiến trúc LLMEmbed")
        self.play(FadeIn(ttl))

        # ---- Văn bản đầu vào ----
        text_box = box("Văn bản\nx", ORANGE, w=1.5, h=1.1, size=22).move_to([-6.0, -0.2, 0])
        self.play(FadeIn(text_box))

        # ---- Các LLM nhẹ (đóng băng) ----
        models = [("Llama2", ACCENT), ("RoBERTa", GREEN), ("BERT", PURPLE)]
        ys = [1.7, -0.2, -2.1]
        stacks, labels = [], []
        for (name, col), y in zip(models, ys):
            st = layer_stack(col).move_to([-3.3, y, 0])
            lb = T(name, 20, col, weight=BOLD).next_to(st, UP, buff=0.1)
            stacks.append(st)
            labels.append(lb)
        llm_group = VGroup(*stacks, *labels)
        in_arrows = [small_arrow(text_box.get_right(), st.get_left(), MUTED, 2.5)
                     for st in stacks]
        self.play(FadeIn(llm_group), *[GrowArrow(a) for a in in_arrows])
        frame_llm = SurroundingRectangle(llm_group, color=MUTED, buff=0.2,
                                         stroke_width=2)
        cap_llm = T("LLM nhẹ – đóng băng\n(không fine-tune)", 18, MUTED)
        cap_llm.next_to(frame_llm, DOWN, buff=0.1).set_x(-4.0)
        self.play(Create(frame_llm), FadeIn(cap_llm))
        self.next_slide()

        # ---- Trích embedding ở nhiều tầng ----
        vecs_all = VGroup()
        extract_anims = []
        for (name, col), st, y in zip(models, stacks, ys):
            v_deep = vec(col).move_to([-0.6, y + 0.3, 0])
            v_shal = vec(col).move_to([-0.6, y - 0.3, 0])
            vecs_all.add(v_deep, v_shal)
            a1 = small_arrow(st[0].get_right(), v_deep.get_left(), col, 3)
            a2 = small_arrow(st[2].get_right(), v_shal.get_left(), col, 3)
            extract_anims += [st[0].animate.set_fill(col, opacity=0.8),
                              st[2].animate.set_fill(col, opacity=0.8),
                              GrowArrow(a1), GrowArrow(a2),
                              FadeIn(v_deep), FadeIn(v_shal)]
        self.play(*extract_anims, run_time=1.5)
        cap_emb = T("Embedding từ\nnhiều tầng / nhiều LLM", 18, ORANGE)
        cap_emb.next_to(vecs_all, DOWN, buff=0.35)
        cap_emb.set_y(-3.35).set_x(0.3)
        self.play(FadeIn(cap_emb))
        self.next_slide()

        # ---- Hợp nhất + Classifier ----
        fusion = box("Hợp nhất\nv(·)", ORANGE, w=1.5, h=1.4, size=22).move_to([2.0, -0.2, 0])
        mlp = box("Classifier\n(MLP)", PURPLE, w=1.5, h=1.4, size=22).move_to([4.1, -0.2, 0])
        out = box("Nhãn\nŷ", GREEN, w=1.3, h=1.0, size=22).move_to([6.1, -0.2, 0])
        fuse_arrows = [small_arrow(v.get_right(), fusion.get_left(), MUTED, 1.5)
                       for v in vecs_all]
        self.play(FadeIn(fusion), *[GrowArrow(a) for a in fuse_arrows])
        self.play(GrowArrow(arrow(fusion, mlp)), FadeIn(mlp))
        self.play(GrowArrow(arrow(mlp, out)), FadeIn(out))
        self.next_slide()

        # ---- Phần nào được huấn luyện? ----
        train_frame = SurroundingRectangle(VGroup(fusion, mlp), color=GREEN,
                                           buff=0.2, stroke_width=3)
        cap_train = T("Chỉ huấn luyện phần này", 20, GREEN, weight=BOLD)
        cap_train.next_to(train_frame, DOWN, buff=0.15)
        self.play(Create(train_frame), FadeIn(cap_train))
        self.next_slide()
