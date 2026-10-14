# Script thiet lap moi truong tu dong cho Windows PowerShell
Write-Host "=== THIET LAP MOI TRUONG MANIM SLIDES ===" -ForegroundColor Cyan

# 1. Kiem tra cong cu quan ly Python
$hasUv = [bool](Get-Command uv -ErrorAction SilentlyContinue)
$hasPy = [bool](Get-Command python -ErrorAction SilentlyContinue)

if ($hasUv) {
    Write-Host "[OK] Phat hien uv da cai dat tren he thong." -ForegroundColor Green
} elseif ($hasPy) {
    Write-Host "[OK] Phat hien python da cai dat tren he thong." -ForegroundColor Green
} else {
    Write-Host "[LOI] Khong tim thay Python hoac uv tren he thong!" -ForegroundColor Red
    exit 1
}

# 2. Tao moi truong ao .venv
if (-not (Test-Path ".venv")) {
    Write-Host "[-] Dang tao moi truong ao .venv..." -ForegroundColor Yellow
    if ($hasUv) {
        uv venv --python 3.12 .venv
    } else {
        python -m venv .venv
    }
    Write-Host "[OK] Da tao .venv thanh cong." -ForegroundColor Green
} else {
    Write-Host "[OK] Moi truong ao .venv da ton tai." -ForegroundColor Green
}

# 3. Cai dat cac goi tu requirements.txt
Write-Host "[-] Dang cai dat cac thu vien can thiet..." -ForegroundColor Yellow
if ($hasUv) {
    uv pip install -r requirements.txt --python .venv\Scripts\python.exe
} else {
    & .venv\Scripts\pip.exe install -r requirements.txt
}
Write-Host "[OK] Da cai dat xong cac thu vien Python." -ForegroundColor Green

# 4. Kiem tra FFmpeg
$hasFfmpeg = [bool](Get-Command ffmpeg -ErrorAction SilentlyContinue)
if ($hasFfmpeg) {
    Write-Host "[OK] FFmpeg da co san tren he thong." -ForegroundColor Green
} else {
    Write-Host "[CANH BAO] Chua tim thay FFmpeg trong PATH." -ForegroundColor Yellow
    Write-Host "    Cai dat nhanh bang: winget install Gyan.FFmpeg" -ForegroundColor Gray
}

# 5. Kiem tra LaTeX (cho s04_math.py)
$hasLatex = [bool]((Get-Command pdflatex -ErrorAction SilentlyContinue) -or (Get-Command latex -ErrorAction SilentlyContinue))
if ($hasLatex) {
    Write-Host "[OK] LaTeX da co san tren he thong." -ForegroundColor Green
} else {
    Write-Host "[THONG TIN] Chua tim thay LaTeX trong PATH." -ForegroundColor DarkYellow
    Write-Host "    File s04_math.py can LaTeX de render MathTex." -ForegroundColor Gray
    Write-Host "    Cac slide s01, s02, s03, s05 khong can LaTeX." -ForegroundColor Gray
    Write-Host "    Cai dat neu can: winget install MiKTeX.MiKTeX" -ForegroundColor Gray
}

Write-Host ""
Write-Host "=== HOAN TAT THIET LAP ===" -ForegroundColor Cyan
Write-Host "Kich hoat moi truong ao bang lenh:" -ForegroundColor Yellow
Write-Host "    .\.venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "Render toan bo slide bang lenh:" -ForegroundColor Yellow
Write-Host "    .\run_all.ps1 -Quality -ql" -ForegroundColor White
