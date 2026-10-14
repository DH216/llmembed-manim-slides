#!/usr/bin/env bash
# Script thiết lập môi trường tự động cho Linux / macOS
set -e

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${CYAN}=== THIẾT LẬP MÔI TRƯỜNG MANIM SLIDES (LINUX / MACOS) ===${NC}"

# 1. Kiểm tra Python hoặc uv
USE_UV=false
if command -v uv &> /dev/null; then
    USE_UV=true
    echo -e "${GREEN}[✓] Phát hiện uv đã cài đặt.${NC}"
elif command -v python3 &> /dev/null; then
    echo -e "${GREEN}[✓] Phát hiện python3 đã cài đặt.${NC}"
else
    echo -e "${RED}[✗] Không tìm thấy Python 3 hoặc uv. Vui lòng cài đặt Python trước!${NC}"
    exit 1
fi

# 2. Tạo môi trường ảo .venv
if [ ! -d ".venv" ]; then
    echo -e "${YELLOW}[-] Đang tạo môi trường ảo .venv...${NC}"
    if [ "$USE_UV" = true ]; then
        uv venv --python 3.12 .venv || uv venv .venv
    else
        python3 -m venv .venv
    fi
    echo -e "${GREEN}[✓] Đã tạo .venv thành công.${NC}"
else
    echo -e "${GREEN}[✓] Môi trường ảo .venv đã tồn tại.${NC}"
fi

# 3. Cài đặt các thư viện từ requirements.txt
echo -e "${YELLOW}[-] Đang cài đặt các thư viện Python từ requirements.txt...${NC}"
if [ "$USE_UV" = true ]; then
    PYTHON_BIN=".venv/bin/python"
    [ -f ".venv/Scripts/python.exe" ] && PYTHON_BIN=".venv/Scripts/python.exe"
    uv pip install -r requirements.txt --python "$PYTHON_BIN"
else
    PIP_BIN=".venv/bin/pip"
    [ -f ".venv/Scripts/pip.exe" ] && PIP_BIN=".venv/Scripts/pip.exe"
    "$PIP_BIN" install -r requirements.txt
fi
echo -e "${GREEN}[✓] Đã cài đặt xong các thư viện Python.${NC}"

# 4. Kiểm tra FFmpeg hệ thống
if command -v ffmpeg &> /dev/null; then
    echo -e "${GREEN}[✓] FFmpeg đã có sẵn trên hệ thống.${NC}"
else
    echo -e "${YELLOW}[!] CẢNH BÁO: Chưa tìm thấy FFmpeg trong PATH.${NC}"
    echo "    Ubuntu/Debian: sudo apt install ffmpeg"
    echo "    Arch Linux:    sudo pacman -S ffmpeg"
    echo "    macOS:         brew install ffmpeg"
fi

# 5. Kiểm tra LaTeX hệ thống (cần cho MathTex)
if command -v pdflatex &> /dev/null || command -v latex &> /dev/null; then
    echo -e "${GREEN}[✓] LaTeX (pdflatex) đã có sẵn trên hệ thống.${NC}"
else
    echo -e "${YELLOW}[i] THÔNG TIN: Chưa tìm thấy LaTeX trong PATH.${NC}"
    echo "    (Slide s04_math.py có cơ chế tự động dùng Text Unicode nếu thiếu LaTeX)."
    echo "    Nếu muốn công thức chuẩn LaTeX:"
    echo "    Ubuntu/Debian: sudo apt install texlive-latex-base texlive-latex-extra texlive-fonts-recommended"
    echo "    macOS:         brew install --cask mactex-no-gui"
fi

echo ""
echo -e "${CYAN}=== HOÀN TẤT THIẾT LẬP ===${NC}"
echo -e "${YELLOW}Kích hoạt môi trường ảo bằng lệnh:${NC}"
echo "    source .venv/bin/activate"
echo -e "${YELLOW}Render toàn bộ slide bằng lệnh:${NC}"
echo "    ./run_all.sh -ql"
