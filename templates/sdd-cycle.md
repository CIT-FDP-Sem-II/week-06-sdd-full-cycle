# The SDD Cycle — One Page

```
   problem statement
          |
          v
    functional spec  <-----------+
          |                      |
          v                      |
  acceptance criteria            | specs change.
          |                      | each change is a
          v                      | commit with a reason.
      test cases                 |
          |                      |
          v                      |
    implementation               |
          |                      |
          v                      |
      evaluation ----------------+
```

## Where this semester sits on it

| Stage | Week |
|---|---|
| Problem statement, functional spec, acceptance criteria | 4 |
| Test cases, failure modes | 5 |
| The full cycle on a new problem, in 45 minutes | **6** |
| Implementation, evaluation | 7 |

## When specs change

They will. Scope creep is not a spec changing — it is a spec changing
**without anyone noticing**.

Three rules:

1. **The spec is in git.** Every change has an author, a date and a diff.
2. **Every change gets a row in the change log**, with the reason. "Because
   the implementation showed FR-4 was impossible as written" is a reason.
   "Updated spec" is not.
3. **A change that adds a requirement must also add or change an acceptance
   criterion.** A requirement nothing tests is a requirement nobody will
   build.

## The three common SDD failures

| Failure | What it looks like | The fix |
|---|---|---|
| **Too rigid** | The spec pins down implementation detail, so every real decision becomes a spec violation | Specify *what*, not *how* |
| **Too vague** | "The system handles errors appropriately" | Binary acceptance criteria |
| **Too large** | 40 requirements, none implemented | Out of Scope section, written first |

Week 7 is where you find out which of the three yours is.
