"""Assemble PROBABILITY_TOOLKIT.md at the repository root from the template and the checked table fragments."""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
text = open(os.path.join(HERE, "PROBABILITY_TOOLKIT.template.md"), encoding="utf-8").read()


def sub(m):
    return open(os.path.join(HERE, m.group(1)), encoding="utf-8").read().rstrip()


out = re.sub(r"\{\{TABLE:([\w.]+)\}\}", sub, text)
assert "{{" not in out
with open(os.path.join(REPO, "PROBABILITY_TOOLKIT.md"), "w", encoding="utf-8", newline="\r\n") as fh:
    fh.write(out)
print("wrote PROBABILITY_TOOLKIT.md", len(out.splitlines()), "lines")
