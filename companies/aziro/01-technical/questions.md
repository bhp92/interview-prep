# Aziro — Technical Round

**Format:** Live interview
**Duration:** ~60 min
**Language used:** Python

---

## Coding Problems

### Q1 — Two Sum

#### Problem
<!-- Add exact problem statement when available -->
Given an array of integers and a target, return indices of two numbers that add up to the target.

#### Approach
Attempted brute force (nested loop O(n²)) and hashmap — struggled with both during the interview.

Optimal approach: hashmap in a single pass O(n).
```python
# For each num, check if (target - num) is already in the map
```

#### Outcome
- [ ] Solved
- [ ] Partial
- [x] Could not solve

#### What to improve
- Classic hashmap pattern: store `{value: index}` as you iterate
- `complement = target - num` — if complement in map, return indices

---

### Q2 — Combination Sum (recursive)

#### Problem
Given a list of candidates and a target, find all combinations of candidates that sum to the target.
The same candidate can be used **multiple times** (unlimited reuse) — this is why the interviewer
said "infinite combinations" (unbounded choices at each step before target is hit).

#### Approach
Attempted brute force — struggled. Correct approach is **backtracking with recursion**.

Key insight: at each step, you either:
1. Include the current candidate again (stay at same index — allows reuse)
2. Move to the next candidate

#### Outcome
- [ ] Solved
- [ ] Partial
- [x] Could not solve

#### What to improve
- Backtracking template: `choose → recurse → unchoose`
- The "infinite" feel comes from unlimited reuse — the recursion terminates only when `remaining == 0` (found) or `remaining < 0` (overshot)

---

## Theory Questions

| # | Question | Outcome |
|---|----------|---------|
| Q3 | What are Decorators? | ✅ Answered |
| Q4 | What are Generators? | ❌ Could not answer |
| Q5 | What is an abstract method? | ✅ Answered |
| Q6 | What is a class method? | ❌ Could not answer |
| Q7 | What is the super() method? | ✅ Answered |
| Q8 | What is inheritance? | ✅ Answered |

> See `solutions/theory.md` for answers and revision notes.