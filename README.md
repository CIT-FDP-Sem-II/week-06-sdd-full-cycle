# Week 6 — SDD in Practice, Full Cycle

**CIT AI-Native Engineering Program · Year 1 · Semester 2 · Module M2**

Blank page to complete spec in 45 minutes. Then the part that matters: doing
by hand what you are about to automate, so that in Week 7 you can tell when
the tool is wrong.

**Lab time: 2 hours. API calls: 2.** See [LAB.md](LAB.md).

## Contents

| Path | What it is |
|---|---|
| `PROBLEM_BRIEF.md` | Three briefs for the sprint, written the way real requests arrive |
| `templates/spec-sprint.md` | Six-component template with a timebox on each section |
| `templates/sdd-cycle.md` | The cycle on one page, plus what to do when specs change |
| `PEER_REVIEW_RUBRIC.md` | 38-point rubric, and the two questions worth more than the score |
| `src/find_ambiguities.py` | The 5-ambiguity prompt. 1 API call. Saves to `findings/` |
| `findings/by-hand.md` | **Your own reading, written before you run anything** |
| `src/gemini_client.py` | Copied forward from Week 2 — unchanged |
| `tests/` | 5 tests on the prompt. No API calls. |

## Why you do it by hand first

Week 7 builds an application that finds spec faults automatically. Week 7 also
asks you which of its findings were **wrong**.

You cannot judge a tool against a standard you never established.
`findings/by-hand.md` is that standard, and its entire value comes from being
written before you read any model output.

Three files go forward to Week 7:

| File | Whose reading |
|---|---|
| `findings/by-hand.md` | Yours |
| `findings/SPEC-model-<stamp>.md` | The one-shot prompt's |
| Week 7 `output/` | Your **application's** |

## The prompt

`src/find_ambiguities.py` holds one prompt, used unchanged all week and again
in Week 7. It is strict about three things, and each one stops a specific
failure:

| Rule | Stops |
|---|---|
| Quote the spec word for word | Findings you cannot check against the source |
| Give a concrete rewrite | "Be more specific" passed off as advice |
| Rank them; find fewer than five if the spec is clean | Padding to hit the number |

That last one matters most. A tool rewarded for finding things will find
things. Test case T7 from Week 5 exists to catch exactly this.

## Running

```powershell
pip install -r requirements.txt
copy .env.example .env                 # mac/linux: cp .env.example .env

python -m pytest tests                 # 5 tests - no API calls
python src/find_ambiguities.py SPEC.md # 1 API call
python src/find_ambiguities.py ../week-04-sdd-specs/SPEC.md
```

> **Not verified in this repo:** `find_ambiguities.py` needs a live key and
> has not been run here. The tests run offline and are verified.

## Free-tier budget

Two calls for the whole lab — one on your sprint spec, one on your Week 4
spec. The script makes exactly one call per run, so re-running is cheap but
not free. Read the output before you re-run it.

## When specs change

Scope creep is not a spec changing. It is a spec changing **without anyone
noticing**. Three rules, in `templates/sdd-cycle.md`:

1. The spec lives in git — every change has an author, a date and a diff.
2. Every change gets a change-log row **with the reason**.
3. A change that adds a requirement must add or change an acceptance
   criterion. A requirement nothing tests is one nobody will build.

---

## Set B (non-IT background)

**`src/find_ambiguities.py`** — one script, three steps.

- `PROMPT` — a block of text telling the model exactly what to look for and
  what shape the answer must take. Most of the work this week is in this
  text, not in the code around it.
- `main()` — reads the spec file you named on the command line, checks it
  exists, builds the client, sends `PROMPT + the spec` as one message, prints
  the reply, and saves it to `findings/` with the date and time in the
  filename so later runs do not overwrite earlier ones.

**`src/gemini_client.py`** — unchanged from Week 2. See that README.

### What Set B may simplify

- The sprint spec may be written in plain English throughout, with **six
  acceptance criteria instead of eight** — but at least two must be failure
  cases.
- The peer review may be done as a conversation, as long as the rubric score
  and the two questions are written down.
- You may find **three** ambiguities by hand rather than five.

### What Set B may **not** simplify

- **`findings/by-hand.md` must be filled in before you run the script.** This
  is the one rule with no exception, because the Week 7 comparison is
  worthless without it.
- You must identify at least one finding you **reject**, with a reason.
  Week 7's `SPEC_REBUILT.md` requires it in writing for both sets.
