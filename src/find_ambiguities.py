"""Ask Gemini to find 5 ambiguities in a specification.

    python src/find_ambiguities.py SPEC.md
    python src/find_ambiguities.py ../week-04-sdd-specs/SPEC.md

Uses 1 API call. The output is saved to findings/ with a timestamp.

IMPORTANT - why you save the output
-----------------------------------
In Week 7 you build an application that does this automatically. You then
have to say which of its findings were right, which it missed, and which it
got wrong.

You cannot judge a tool against a standard you never wrote down. The file this
script saves, plus the one you fill in BY HAND in findings/by-hand.md, is that
standard. Keep both.
"""

import sys
from datetime import datetime
from pathlib import Path

from gemini_client import GeminiClient, MissingKeyError

ROOT = Path(__file__).parent.parent
FINDINGS = ROOT / "findings"

# One prompt, used unchanged all week. It is deliberately strict about three
# things, because without them the model pads:
#   - exactly five, so it has to rank rather than list everything
#   - a quote from the spec, so a finding can be checked against the source
#   - a concrete rewrite, so "be more specific" is not an acceptable answer
PROMPT = """You are reviewing a software specification for ambiguity.

Find exactly FIVE problems. For each one, use this format:

AMBIGUITY <n>
QUOTE: "<the exact wording from the specification>"
PROBLEM: <why two engineers could read this differently>
REWRITE: <a concrete replacement that removes the ambiguity>

Rules:
- Quote the specification word for word. Do not paraphrase.
- Do not report a problem you cannot quote.
- Rank them: the most damaging ambiguity is number 1.
- "Be more specific" is not a rewrite. Write the actual replacement text.
- If the specification is genuinely clear in a section, do not invent a
  problem there. Say so and give fewer than five.

SPECIFICATION:
"""


def main():
    if len(sys.argv) < 2:
        print("usage: python src/find_ambiguities.py <path to spec>")
        return 1

    spec_path = Path(sys.argv[1])
    if not spec_path.is_file():
        print(f"Cannot find {spec_path}")
        return 1

    spec_text = spec_path.read_text(encoding="utf-8")

    try:
        client = GeminiClient()
    except MissingKeyError as exc:
        print(f"STOPPED: {exc}")
        return 1

    print(f"Reviewing {spec_path} ({len(spec_text.split())} words). 1 API call.\n")
    findings = client.ask(PROMPT + spec_text)
    print(findings)

    FINDINGS.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d-%H%M")
    out = FINDINGS / f"{spec_path.stem}-model-{stamp}.md"
    out.write_text(
        f"# Model findings: {spec_path.name}\n\n"
        f"Generated {stamp}. Prompt is unchanged from src/find_ambiguities.py.\n\n"
        f"{findings}\n",
        encoding="utf-8",
    )
    print(f"\nSaved to {out}")
    print("Keep this file. Week 7 compares your application's findings against it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
