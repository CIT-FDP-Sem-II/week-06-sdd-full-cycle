# Week 6 Lab — SDD in Practice, Full Cycle

**Time: 2 hours · API calls used: 2**

| # | Activity | Time | Code? |
|---|----------|------|-------|
| 1 | Spec sprint — blank page to complete spec | 45 min | no |
| 2 | Use the model to challenge your spec | 10 min | run only (1 call) |
| 3 | Peer review — swap specs | 20 min | no |
| 4 | By-hand ambiguity pass on your Week 4 spec | 15 min | no |
| 5 | Run the same prompt, compare, save both | 20 min | run only (1 call) |
| 6 | What you would change | 10 min | no |

---

## 1. Spec sprint (45 min, no code)

Faculty hands out a brief from [PROBLEM_BRIEF.md](PROBLEM_BRIEF.md). Write a
complete spec — all six components — in 45 minutes, using
`templates/spec-sprint.md`.

The template has a timebox on each section. **Keep to them.** A complete rough
spec beats a beautiful half-finished one; you cannot peer-review Section 5 if
it is empty.

Spend the first five minutes listing what the brief does **not** tell you.
Every brief hides the same four gaps: what the input is exactly, what counts
as done, what the quality words mean, and what happens when it fails. Briefs
never mention failure.

Where you cannot answer, **write down the assumption and move on**. An
assumption stated in Section 1 is a decision. An assumption left unstated is
a bug in three weeks.

---

## 2. Use the model to challenge your spec (10 min, 1 API call)

```powershell
python src/find_ambiguities.py <your sprint spec>
```

Five ambiguities, each with a quote, a problem and a rewrite.

Read them critically. The prompt deliberately gives the model permission to
find **fewer** than five — if yours still returns exactly five on a clean
section, that is a finding about the tool, not about your spec.

---

## 3. Peer review (20 min, no code)

Swap specs. Score your partner's against
[PEER_REVIEW_RUBRIC.md](PEER_REVIEW_RUBRIC.md) — 38 points across the six
sections.

Then answer the two questions that matter more than the score:

1. **Which requirement would you build wrong?** Find the one you could
   implement in good faith and still deliver the wrong thing.
2. **Which acceptance criterion could you pass without satisfying the
   requirement it claims to test?** A criterion that is binary *and* mapped
   *and* still misses the point is the most dangerous kind, because it looks
   finished.

Giving the feedback: quote before you judge, say what would fix it, and label
preference as preference.

---

## 4. By-hand ambiguity pass (15 min, no code)

**Before you run anything.** Open `findings/by-hand.md` and find five
ambiguities in your own **Week 4** `SPEC.md` — the Spec Review Assistant one.

Yourself. On paper. No model.

This file is what Week 7 compares against. Fill it in after reading model
output and it is worthless, and so is the Week 7 comparison.

Found only three? Write three, and say so. "My spec genuinely has three" is a
legitimate result — and it makes the Week 5 test case T7 much more
interesting when the tool reports five.

---

## 5. Run the same prompt and compare (20 min, 1 API call)

```powershell
python src/find_ambiguities.py ../week-04-sdd-specs/SPEC.md
```

Output is saved to `findings/` with a timestamp. **Keep it.**

Now fill in the comparison table in `findings/by-hand.md`:

| | Count |
|---|---|
| Both found it | |
| Only I found it | |
| Only the model found it | |
| Model found it and was wrong | |

That last row is the one to work at. There is almost always at least one. If
you cannot find it, you are deferring to the output rather than reading it.
Look for a "quote" that is not in your spec word for word, a problem your Out
of Scope section already answers, or a rewrite that is more specific but less
correct.

---

## 6. What you would change (10 min)

One paragraph at the bottom of `findings/by-hand.md`: **which findings will
you act on, and which are you rejecting?**

You need at least one rejection, with a reason. In Week 7 the assessment
requires it in writing — `SPEC_REBUILT.md` must contain at least one rejected
finding and why. Start the habit now.

---

## Before you leave

- [ ] A complete six-component spec written from a blank page in 45 minutes
- [ ] Assumptions written down where the brief was silent
- [ ] Model challenge run on the sprint spec, output read critically
- [ ] Partner's spec scored out of 38, and both questions answered
- [ ] **`findings/by-hand.md` filled in before running the script**
- [ ] Script run on your Week 4 `SPEC.md`, output **saved**
- [ ] Comparison table filled in, including "model was wrong"
- [ ] At least one finding rejected, with a reason

## Looking ahead

Week 7 implements the Week 4 spec against the Week 5 test suite, then compares
its findings against the two files you saved today. The question in Week 7 is
not "did it work". It is **"can I tell when it is wrong?"** — and today is
when you earned the right to answer that.
