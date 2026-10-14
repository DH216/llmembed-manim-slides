# Slide Manim: LLMEmbed (ACL 2024)

Bài báo: *LLMEmbed: Rethinking Lightweight LLM's Genuine Function in Text Classification*
(Chun Liu et al.) — https://aclanthology.org/2024.acl-long.433

## Cài đặt

```bash
pip install "manim==0.19.0" manim-slides
```

Nên ghim `manim==0.19.0`: bản `manim-slides` 5.7 đã thử không chạy với `manim` 0.22 (lỗi `write_to_movie`).
Cần thêm thư viện hệ thống cho Manim (cairo, pango, ffmpeg) – xem docs.manim.community.

`s04_math.py` dùng `MathTex` nên cần cài LaTeX (TeX Live / MiKTeX). Các file còn lại không cần LaTeX.

## Cấu trúc

| File | Scene | Nội dung |
|---|---|---|
| `common.py` | – | màu sắc, helper, lớp `BaseSlide` |
| `s01_intro.py` | `S01Title`, `S01Problem` | tiêu đề, mục lục, động cơ |
| `s02_paradigm.py` | `S02Paradigm` | prompt-based vs LLMEmbed |
| `s03_pipeline.py` | `S03Pipeline` | kiến trúc: trích xuất đa tầng → hợp nhất → classifier |
| `s04_math.py` | `S04Math` | công thức chính |
| `s05_results.py` | `S05Efficiency`, `S05Takeaways` | hiệu quả (4% / 1.8% / 1.5%), kết luận |

## Render và trình chiếu

```bash
chmod +x run_all.sh
./run_all.sh          # render chất lượng thấp (nhanh)
./run_all.sh -qh      # render chất lượng cao

manim-slides present S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways
# hoặc xuất HTML:
manim-slides convert S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways llmembed.html
```

Trong lúc trình chiếu, bấm phím mũi tên phải để sang bước tiếp theo.

## Lưu ý

- Nếu chữ tiếng Việt bị lỗi dấu, đặt `FONT = "Arial"` (hoặc font bạn có) trong `common.py`.
- Các công thức và số liệu hiệu quả lấy từ abstract và mô tả phương pháp của bài báo. Hãy đối chiếu với
  bản PDF (đặc biệt hàm hợp nhất `v(·)`, chi tiết chọn tầng, và bảng kết quả trên các dataset) rồi bổ sung
  thêm slide kết quả theo số liệu gốc.
