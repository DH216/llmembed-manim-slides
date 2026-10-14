# Render tất cả scene trên Windows PowerShell
# Cách dùng: .\run_all.ps1 [-Quality -ql|-qm|-qh] (mặc định là -ql)
param (
    [string]$Quality = "-ql"
)

$ErrorActionPreference = "Stop"

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "Đang render slide với chất lượng $Quality..." -ForegroundColor Cyan

$manimCmd = "manim"
if (Test-Path ".\.venv\Scripts\manim.exe") {
    $manimCmd = ".\.venv\Scripts\manim.exe"
}

& $manimCmd $Quality s01_intro.py S01Title S01Problem
& $manimCmd $Quality s02_paradigm.py S02Paradigm
& $manimCmd $Quality s03_pipeline.py S03Pipeline

& $manimCmd $Quality s04_math.py S04Math
& $manimCmd $Quality s05_results.py S05Efficiency S05Takeaways

Write-Host "`nĐã hoàn thành quá trình render toàn bộ slide!" -ForegroundColor Green

$sceneList = "S01Title S01Problem S02Paradigm S03Pipeline S04Math S05Efficiency S05Takeaways"

Write-Host "Để trình chiếu, chạy lệnh sau:" -ForegroundColor Yellow
Write-Host "manim-slides present $sceneList" -ForegroundColor White
Write-Host "`nHoặc xuất sang file HTML:" -ForegroundColor Yellow
Write-Host "manim-slides convert $sceneList llmembed.html" -ForegroundColor White
