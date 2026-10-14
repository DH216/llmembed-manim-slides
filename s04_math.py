from common import *
import shutil

has_latex = bool(shutil.which("latex") or shutil.which("pdflatex"))


class S04Math(BaseSlide):
    def construct(self):
        ttl = title("Công thức chính")
        self.play(FadeIn(ttl))

        rows_spec = [
            (r"\phi_i^{(m,d_m)} = f\left(x_i \mid m,\, d_m\right)",
             "ϕ_i^(m, d_m) = f(x_i | m, d_m)",
             "Trích embedding của văn bản x_i từ LLM m tại tầng d_m (LLM đóng băng)"),
            (r"\psi_i = v\left(\phi_i^{(m_1,d_1)},\, \dots,\, \phi_i^{(m_k,d_k)}\right)",
             "ψ_i = v(ϕ_i^(m_1, d_1), ..., ϕ_i^(m_k, d_k))",
             "Hợp nhất embedding từ nhiều LLM / nhiều độ sâu thành một vector ψ_i"),
            (r"\tilde{y}_i = g_{\theta}(\psi_i)",
             "ỹ_i = g_θ(ψ_i)",
             "Classifier nhẹ g_θ dự đoán nhãn – chỉ phần này được huấn luyện"),
            (r"\arg\min_{\theta}\; \mathcal{L} = -\sum_i y_i \log \tilde{y}_i",
             "arg min_θ  L = - ∑ y_i · log(ỹ_i)",
             "Hàm mất mát cross-entropy"),
        ]

        rows = VGroup()
        for eq_tex, eq_unicode, cap in rows_spec:
            if has_latex:
                eq = MathTex(eq_tex, font_size=40, color=FG)
            else:
                eq = T(eq_unicode, 34, weight=BOLD, color=FG)
            cp = T(cap, 22, MUTED)
            if cp.width > 12:
                cp.scale_to_fit_width(12)
            rows.add(VGroup(eq, cp).arrange(DOWN, buff=0.15))
        rows.arrange(DOWN, buff=0.55).next_to(ttl, DOWN, buff=0.5)

        colors = [ACCENT, ORANGE, PURPLE, GREEN]
        for row, col in zip(rows, colors):
            row[0].set_color(col)
            self.play(Write(row[0]))
            self.play(FadeIn(row[1], shift=UP * 0.1))
            self.next_slide()
