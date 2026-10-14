# Slide Manim: LLMEmbed (ACL 2024)

Bài báo: *LLMEmbed: Rethinking Lightweight LLM's Genuine Function in Text Classification*  
(Chun Liu et al.) — https://aclanthology.org/2024.acl-long.433

Dự án slide hoạt họa trực quan hóa bài báo khoa học bằng **Manim** và **Manim-Slides**, hỗ trợ đa nền tảng (**Linux**, **Windows**, **macOS**).

---

## 1. Cài đặt phụ thuộc hệ thống (System Prerequisites)

### Trên Linux (Ubuntu / Debian):
```bash
sudo apt update
sudo apt install -y ffmpeg texlive-latex-base texlive-latex-extra texlive-fonts-recommended
```

### Trên Windows (PowerShell):
```powershell
winget install Gyan.FFmpeg MiKTeX.MiKTeX
```
*(Lưu ý: Sau khi cài trên Windows, hãy mở lại cửa sổ PowerShell mới để nhận diện PATH).*

### Trên macOS (Homebrew):
```bash
brew install ffmpeg mactex-no-gui
```

---

## 2. Thiết lập môi trường Python

Dự án hỗ trợ script thiết lập tự động (tự nhận diện `uv` hoặc `python`):

### Trên Linux / macOS:
```bash
chmod +x setup_env.sh run_all.sh
./setup_env.sh
source .venv/bin/activate
```

### Trên Windows (PowerShell):
```powershell
.\setup_env.ps1
.\.venv\Scripts\Activate.ps1
```

*(Hoặc cài đặt thủ công: `pip install -r requirements.txt`).*

---

## 3. Cấu trúc bài thuyết trình

| Tệp tin | Scene | Nội dung |
|---|---|---|
| `common.py` | – | Bảng màu dark mode, helper mobject, cấu hình font tự động đa nền tảng |
| `s01_intro.py` | `S01Title`, `S01Problem` | Tiêu đề, tác giả, mục lục, động cơ nghiên cứu |
| `s02_paradigm.py` | `S02Paradigm` | So sánh cơ chế Prompt-based vs LLMEmbed |
| `s03_pipeline.py` | `S03Pipeline` | Kiến trúc đường ống: trích xuất đa tầng → hợp nhất → classifier MLP |
| `s04_math.py` | `S04Math` | Công thức toán học (MathTex với fallback Unicode tự động nếu thiếu LaTeX) |
| `s05_results.py` | `S05Efficiency`, `S05Takeaways` | Hiệu quả tính toán (4% param / 1.8% energy / 1.5% time), kết luận |

---

## 4. Render toàn bộ slide

- **Trên Linux / macOS / Git Bash**:
  ```bash
  ./run_all.sh -ql      # Render nhanh chất lượng thấp (480p)
  ./run_all.sh -qh      # Render chất lượng cao (1080p)
  ```
- **Trên Windows PowerShell**:
  ```powershell
  .\run_all.ps1 -Quality -ql   # Render nhanh (480p)
  .\run_all.ps1 -Quality -qh   # Render chất lượng cao (1080p)
  ```

---

## 5. Trình chiếu slide (Presenting)

### Cách 1: Trình chiếu dạng ứng dụng desktop
```bash
manim-slides present S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways
```
- Phím `Space` hoặc `→`: Chuyển hiệu ứng / slide tiếp theo.
- Phím `←`: Quay lại hiệu ứng trước.
- Phím `F`: Bật / tắt chế độ toàn màn hình (Full Screen).
- Phím `Q`: Thoát trình chiếu.

### Cách 2: Mở xem trực tiếp trên trình duyệt web (HTML)
```bash
manim-slides convert S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways llmembed.html
```
Sau đó mở tệp `llmembed.html` bằng trình duyệt (Chrome, Firefox, Edge, Safari).
