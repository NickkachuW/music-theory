"""
Fill in strudel.cc share links in a workbook markdown file.

Each `[... ](strudel:auto)` placeholder is replaced with a share URL for the
nearest preceding ```js code block. Strudel's URL format (packages/core/util.mjs):
    https://strudel.cc/#<encodeURIComponent(base64(utf8(code)))>
Re-running is safe: existing strudel.cc links are regenerated from the current
code blocks, so edit a snippet and re-run to refresh its link.

Usage: python make_links.py module-1-rhythm.md
"""
import base64
import re
import sys
from urllib.parse import quote

def code_to_url(code: str) -> str:
    b64 = base64.b64encode(code.encode("utf-8")).decode("ascii")
    return "https://strudel.cc/#" + quote(b64, safe="")

def fill_links(text: str) -> tuple[str, int]:
    # Normalize previously generated links back to placeholders so re-runs refresh them
    text = re.sub(r"\(https://strudel\.cc/#[^)]*\)", "(strudel:auto)", text)
    parts = re.split(r"(```js\n.*?```)", text, flags=re.S)
    out, last_code, count = [], None, 0
    for part in parts:
        m = re.fullmatch(r"```js\n(.*?)```", part, flags=re.S)
        if m:
            last_code = m.group(1).rstrip("\n")
            out.append(part)
            continue
        while "(strudel:auto)" in part:
            if last_code is None:
                raise SystemExit("Placeholder before any ```js block")
            part = part.replace("(strudel:auto)", f"({code_to_url(last_code)})", 1)
            count += 1
        out.append(part)
    return "".join(out), count

if __name__ == "__main__":
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        text = f.read()
    text, count = fill_links(text)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"{path}: {count} links generated")
