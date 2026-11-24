# Problem Brief — Spec Sprint

**Faculty hands this out at the start of the lab. 45 minutes, blank page to
complete spec.**

Three briefs are given below. Faculty picks one on the day, or supplies
another. Each is deliberately written the way a real request arrives: as a
paragraph from someone who has not thought about edge cases.

---

## Brief 1 — The reading list checker

> "Our lecturers upload reading lists as plain text. Half the links are dead
> by the time students get to them. We want something that checks a reading
> list and tells the lecturer which entries are broken, so they can fix them
> before term starts. It should be quick — nobody will use it if it takes
> ages."

---

## Brief 2 — The lab booking assistant

> "Students book lab slots by emailing the technician, who keeps a
> spreadsheet. It's chaos. We want students to be able to ask in plain
> English — 'can I get the 3D printer on Thursday afternoon' — and get a
> straight answer. Obviously it mustn't double-book anything."

---

## Brief 3 — The feedback summariser

> "We get about 400 free-text comments per module in the end-of-term survey.
> Nobody reads them properly. We want a summary that tells the module leader
> what students actually said, without losing the minority views — last year
> somebody summarised 'mostly positive' and missed four separate complaints
> about the same broken equipment."

---

## What you have to produce

A complete spec, all six components, in 45 minutes. Use
`templates/spec-sprint.md`.

## The four questions the brief does not answer

Every one of these briefs hides the same kinds of gap. Before you write
anything, spend five minutes listing what you are **not** told:

1. **What is the input, exactly?** Brief 1 says "plain text" — one file? A
   folder? What does an entry look like?
2. **What counts as done?** Brief 1 says "broken" — a 404? A redirect? A
   paywall? A link that works but points at the wrong edition?
3. **What does the quality word mean?** "Quick", "straight answer",
   "without losing minority views" — all three need a number or a rule.
4. **What happens when it fails?** None of the three briefs mentions failure
   at all. They never do.

You will not be able to answer all of these. **That is the point.** Where you
cannot, write down the assumption you made and move on — an assumption stated
in Section 1 is a decision; an assumption left unstated is a bug in three
weeks' time.
