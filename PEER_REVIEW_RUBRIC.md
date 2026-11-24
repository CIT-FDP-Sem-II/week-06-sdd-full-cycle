# Peer Review Rubric

Swap specs. 20 minutes. Score your partner's, then talk.

**Score each line 0 / 1 / 2.** 0 = absent, 1 = present but weak, 2 = solid.

---

## 1. Problem Statement (max 6)

| | Check | Score |
|---|---|---|
| 1.1 | The problem is stated, not just the solution | |
| 1.2 | It says **who** it is for, specifically | |
| 1.3 | Something is explicitly marked **not** a goal | |

## 2. Functional Requirements (max 8)

| | Check | Score |
|---|---|---|
| 2.1 | Numbered, so criteria can point at them | |
| 2.2 | One behaviour per requirement (no hidden "and") | |
| 2.3 | They say **what**, not **how** | |
| 2.4 | Nothing essential is missing — could you build from these alone? | |

## 3. Non-Functional Requirements (max 6)

| | Check | Score |
|---|---|---|
| 3.1 | **Every one carries a number** | |
| 3.2 | They cover more than speed (security, failure, size, cost) | |
| 3.3 | The numbers are defensible, not invented to fill the box | |

## 4. Out of Scope (max 4)

| | Check | Score |
|---|---|---|
| 4.1 | Present at all | |
| 4.2 | Excludes something a reader would plausibly have assumed | |

## 5. Acceptance Criteria (max 10)

| | Check | Score |
|---|---|---|
| 5.1 | Every one is **binary** — you can say how you would run it | |
| 5.2 | Every one maps to a numbered requirement | |
| 5.3 | **At least two are failure cases** | |
| 5.4 | They cover the requirements, not just the easy ones | |
| 5.5 | None of them needs a judgement call to score | |

## 6. Evaluation (max 4)

| | Check | Score |
|---|---|---|
| 6.1 | Says how you would know the system is **good**, not just correct | |
| 6.2 | Names at least one thing the testing does **not** cover | |

---

**Total: ____ / 38**

| Score | Reading |
|---|---|
| 30–38 | Could be handed to someone else to build |
| 20–29 | Buildable, but expect three arguments during implementation |
| Under 20 | The gaps will be found by the code, which is the expensive way |

---

## The two questions that matter more than the score

Write a sentence for each. These are what your partner actually takes away.

### 1. Which requirement would you build wrong?

> Find the one you could implement in good faith and still deliver something
> your partner did not want. Quote it.

### 2. Which acceptance criterion could you pass without satisfying the
### requirement it claims to test?

> This is the most useful thing a reviewer finds. A criterion that is binary
> *and* mapped *and* still misses the point is the most dangerous kind,
> because it looks finished.

---

## How to give the feedback

Three rules, borrowed from code review:

1. **Quote before you judge.** "Section 3 says 'fast'" beats "the NFRs are vague".
2. **Say what would fix it.** A finding with no suggested rewrite is a complaint.
3. **Separate fact from preference.** "AC-4 is not binary" is a fact.
   "I'd have scoped this differently" is a preference — still worth saying,
   but label it.
