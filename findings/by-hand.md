# By-Hand Findings — Week 4 Spec Review Assistant Spec

**Fill this in yourself, before you run the script. 15 minutes.**

This is the file Week 7 compares against. Its whole value is that **you wrote
it without a model's help**. If you fill it in after reading the model output,
it is worthless and so is the Week 7 comparison.

---

## The five ambiguities I found by hand

Target: your own Week 4 `SPEC.md` for the Spec Review Assistant.

| # | Quote from the spec | Why it is ambiguous | My rewrite |
|---|---------------------|---------------------|------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

**Found fewer than five?** Say so, and say why — "my spec genuinely has three"
is a legitimate result, and it makes T7 in the Week 5 test suite much more
interesting. (T7 asks whether the tool invents faults in a clean spec. If you
honestly believe your spec only has three ambiguities, and the tool reports
five, you have just learned something about the tool.)

---

## Then run the script

```powershell
python src/find_ambiguities.py ../week-04-sdd-specs/SPEC.md
```

One API call. The output is saved to `findings/` with a timestamp.

---

## The comparison (do this now, while it is fresh)

| | Count | Which ones |
|---|---|---|
| **Both found it** | | |
| **Only I found it** | | |
| **Only the model found it** | | |
| **Model found it and was wrong** | | |

### The one the model found that I missed

> Quote it. Was it a real problem, or did it just sound like one?

### The one I found that the model missed

> Quote it. Why do you think it missed it — was the ambiguity about something
> outside the text, like a domain assumption?

### The one the model got wrong

> There is almost always at least one. If you cannot find it, you are
> deferring to the output rather than reading it. Look specifically for:
> - a "quote" that is not actually in your spec word for word
> - a problem that your Out of Scope section already answers
> - a rewrite that is more specific but less correct

---

## Carry all three files to Week 7

| File | What it is |
|---|---|
| `findings/by-hand.md` | This file — your own reading |
| `findings/SPEC-model-<stamp>.md` | The script's output |
| Week 7 `output/` | What your **application** finds |

In Week 7 you compare all three. The question is not "did the application
work". It is **"can I tell when it is wrong?"** — and you can only answer that
because of the fifteen minutes you spent on this page.
