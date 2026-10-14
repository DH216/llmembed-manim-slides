#!/usr/bin/env bash
# Render tất cả scene trên Linux/macOS hoặc Git Bash.
# Cách dùng: ./run_all.sh [-ql|-qm|-qh] (mặc định: -ql)
set -e

Q="${1:--ql}"

echo -e "\033[0;36m=== Đang render slide Manim với chất lượng ${Q}... ===\033[0m"

MANIM_CMD="manim"
if [ -f "./.venv/bin/manim" ]; then
    MANIM_CMD="./.venv/bin/manim"
elif [ -f "./.venv/Scripts/manim.exe" ]; then
    MANIM_CMD="./.venv/Scripts/manim.exe"
fi

$MANIM_CMD "$Q" s01_intro.py S01Title S01Problem
$MANIM_CMD "$Q" s02_paradigm.py S02Paradigm
$MANIM_CMD "$Q" s03_pipeline.py S03Pipeline
$MANIM_CMD "$Q" s04_math.py S04Math
$MANIM_CMD "$Q" s05_results.py S05Efficiency S05Takeaways

echo ""
echo -e "\033[0;32m[✓] Đã render xong tất cả slide!\033[0m"
echo -e "\033[1;33mTrình chiếu bằng lệnh:\033[0m"
echo "    manim-slides present S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways"
echo -e "\033[1;33mHoặc xuất ra file HTML:\033[0m"
echo "    manim-slides convert S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways llmembed.html"
