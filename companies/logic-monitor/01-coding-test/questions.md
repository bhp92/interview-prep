# LogicMonitor — Coding Test

**Platform:** Qualified.io
**Link:** https://www.qualified.io/assess/5d30c3ceccd7c8001355109c?invite=girdzG6hzaTFOw
**Duration:** 1 hour
**Language used:** Python

---

## Q1 — Unique character in string

### Problem
Find the first unique character in a string and return it in its original case.

### Approach
Brute force O(n²) — nested loop comparing each character. Took ChatGPT help to finish.
Optimal approach missed: use `Counter` or hash map for O(n).

### Outcome
- [ ] Passed all test cases
- [x] Partial — submitted brute force, unclear if all cases passed
- [ ] Failed

### What to improve
- Practice string frequency problems with Counter
- `collections.Counter(s.lower())` would solve this cleanly in O(n)

---

## Q2 — Mask account number

### Problem
Mask all characters of an account number except the last 4 with `*`.
If length <= 4, return as-is.

### Approach
Did not attempt — only saw this with 2 minutes remaining.

### Outcome
- [ ] Passed all test cases
- [ ] Partial
- [x] Did not attempt

### What to improve
- Simple string slicing: `'*' * (len(s) - 4) + s[-4:]`
- Would have been the easiest problem on the test

---

## Q3 — Unknown

### Problem
Not seen — ran out of time.

### Outcome
- [x] Did not attempt