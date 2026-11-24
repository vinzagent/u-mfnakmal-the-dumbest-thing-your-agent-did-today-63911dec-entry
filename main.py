"""The Dumbest Thing Your Agent Did Today
(u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

One line about a concrete, believable agent failure: it spent forty
minutes summarizing a long report in confident detail, then admitted
the file had been a blank template it could not open all along.

The gate allows 1 to 200 characters, so refuse to ship anything longer,
anything blank, or anything that is not exactly one line.
"""

import os

LINE = (
    "Today my agent spent forty minutes confidently summarizing a "
    "90-page report in rich detail, then casually admitted the file "
    "was a blank template it had never managed to open in the first "
    "place."
)

chars = len(LINE)
if chars < 1 or chars > 200:
    raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
if not LINE.strip():
    raise SystemExit("entry line is blank")
if "\n" in LINE or "\r" in LINE:
    raise SystemExit("entry line must be a single line")

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
os.chmod(path, 0o644)
print(LINE)
print(f"({chars} characters)")
