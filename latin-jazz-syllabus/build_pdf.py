"""
Build Latin_Jazz_Tango_Syllabus.pdf:
  1. run generate_pdf.py                  -> text/tables (cover, phases, daily routine)
  2. run generate_chord_progressions.py   -> chord_progressions.pdf
  3. run generate_tune_analysis.py        -> tune_analysis.pdf
  4. run lilypond on the two .ly files    -> engraved riff PDFs
  5. concat in order: text, chord, tune, riffs, riffs-12-keys
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parent
SHEET = ROOT / "sheet-music"
TEXT_PDF = ROOT / "Latin_Jazz_Tango_Syllabus_text.pdf"
FINAL_PDF = ROOT / "Latin_Jazz_Tango_Syllabus.pdf"

LILY = shutil.which("lilypond") or r"C:\Users\nicwo\AppData\Local\Microsoft\WinGet\Packages\LilyPond.LilyPond_Microsoft.Winget.Source_8wekyb3d8bbwe\lilypond-2.24.4\bin\lilypond.exe"


def run(cmd, cwd=None):
    print(f"+ {' '.join(str(c) for c in cmd)}")
    subprocess.check_call(cmd, cwd=cwd)


def main():
    # 1. text PDF — generate_pdf.py writes to FINAL_PDF directly; rename to intermediate.
    run([sys.executable, str(ROOT / "generate_pdf.py")])
    if FINAL_PDF.exists():
        shutil.move(str(FINAL_PDF), str(TEXT_PDF))

    # 2 + 3. chord progressions + tune analysis (each writes its own .pdf next to source)
    run([sys.executable, str(ROOT / "generate_chord_progressions.py")])
    run([sys.executable, str(ROOT / "generate_tune_analysis.py")])

    # 4. engrave both .ly files
    for ly in ("riffs_and_licks.ly", "riffs_all_12_keys.ly"):
        run([LILY, "--output", str(SHEET / Path(ly).stem), str(SHEET / ly)],
            cwd=SHEET)

    # 5. concat
    sources = [
        TEXT_PDF,
        ROOT / "chord_progressions.pdf",
        ROOT / "tune_analysis.pdf",
        SHEET / "riffs_and_licks.pdf",
        SHEET / "riffs_all_12_keys.pdf",
    ]
    writer = PdfWriter()
    for src in sources:
        writer.append(str(src))
    page_count = len(writer.pages)
    with open(FINAL_PDF, "wb") as f:
        writer.write(f)

    TEXT_PDF.unlink(missing_ok=True)
    print(f"\nWrote {FINAL_PDF} ({page_count} pages)")


if __name__ == "__main__":
    main()
