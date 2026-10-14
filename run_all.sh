#!/usr/bin/env bash
# Render tất cả scene. Dùng: ./run_all.sh [-ql|-qm|-qh]
Q="${1:--ql}"
set -e
manim $Q s01_intro.py S01Title S01Problem
manim $Q s02_paradigm.py S02Paradigm
manim $Q s03_pipeline.py S03Pipeline
manim $Q s04_math.py S04Math
manim $Q s05_results.py S05Efficiency S05Takeaways
echo "Xong. Trình chiếu: manim-slides present S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways"
