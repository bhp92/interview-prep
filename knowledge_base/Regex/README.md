# Regex — Python & Shell Study

This repository is my practical study reference for Regular Expressions,
with a focus on using regex confidently in:

- Python
- Bash / shell scripting
- grep
- grep -E
- sed
- awk
- Bash `[[ string =~ regex ]]`

The goal is not to become a regex specialist or learn obscure regex
features.

The goal is to develop strong practical regex understanding appropriate
for an experienced IT professional:

- understand how regex works conceptually
- read regex patterns without memorizing them mechanically
- construct patterns from requirements
- understand why a pattern works or fails
- debug regexes
- use regex effectively in Python
- use regex effectively in shell scripting
- understand differences between regex dialects
- recognize advanced regex features when encountered

---

# Repository Structure

```text
regex/
│
├── README.md
├── 01_regex_fundamentals.md
├── 02_python_regex.md
├── 03_bash_regex.md
├── 04_test_data.txt
└── 05_exercises.md
```

## Files

### `01_regex_fundamentals.md`

Contains the regex language itself:

* regex mental model
* literals
* character matching
* character classes
* shorthand classes
* anchors
* quantifiers
* grouping
* alternation
* boundaries
* escaping
* greedy/lazy matching
* other core regex concepts

This file should describe regex independently of Python or Bash
wherever possible.

---

### `02_python_regex.md`

Contains Python-specific regex knowledge:

* `re` module
* `re.search`
* `re.match`
* `re.fullmatch`
* `re.findall`
* `re.finditer`
* `re.sub`
* match objects
* capturing groups
* named groups
* flags
* Python raw strings
* Python-specific regex behavior
* practical Python examples
* regex debugging in Python

---

### `03_bash_regex.md`

Contains shell-specific regex knowledge:

* regex vs shell globbing
* `grep`
* Basic Regular Expressions (BRE)
* `grep -E`
* Extended Regular Expressions (ERE)
* Bash `[[ string =~ regex ]]`
* quoting considerations
* `sed`
* `awk`
* practical shell examples
* differences between shell tools and Python regex

---

### `04_test_data.txt`

A collection of realistic text/data that can repeatedly be used
for exercises.

Examples:

* names
* email-like strings
* phone numbers
* dates
* IP addresses
* log entries
* file paths
* URLs
* error messages
* configuration-like text
* multiline logs
* deliberately malformed data

The same data should be usable from both Python and shell.

---

### `05_exercises.md`

Contains exercises designed to progressively cover the material.

Exercises should not merely ask:

"What does `\d` mean?"

They should increasingly require:

* constructing regexes
* predicting matches
* explaining why something does not match
* extracting information
* validating input
* searching text
* replacing text
* translating a requirement into regex
* using the same regex in Python and shell where appropriate

---

# Learning Philosophy

The course should be taught interactively.

Do NOT simply dump a large regex tutorial.

The preferred learning loop is:

```text
Concept
   ↓
Explanation
   ↓
Small examples
   ↓
User constructs patterns
   ↓
User explains patterns
   ↓
Correction / refinement
   ↓
Add learned material to the appropriate file
   ↓
Move to next concept
```

The user learns best by constructing and explaining regexes rather
than memorizing syntax.

Definitions should be descriptive and precise rather than extremely
short keyword definitions.

---

# Important Teaching Rules

## 1. Do not jump ahead

A concept is considered learned only after:

1. it has been explained,
2. examples have been discussed,
3. the user has practiced it,
4. mistakes have been corrected.

Mentioning a concept does NOT mean it has been learned.

For example:

Lazy quantifiers may be mentioned while discussing greedy matching,
but they should not be treated as completed until they have been
properly explained and practiced.

---

## 2. Maintain the Markdown carefully

The Markdown files are the permanent reference.

Only add material after the concept has been taught.

When adding material, explicitly tell the user:

* which file to update
* where to add it
* the exact Markdown content

Do not silently reorganize or rewrite previously written material.

If existing content is missing something, identify the missing content
and provide an exact block to add.

---

## 3. Do not duplicate concepts unnecessarily

The fundamentals file should contain the regex language itself.

Python-specific behavior belongs in:

```text
02_python_regex.md
```

Shell-specific behavior belongs in:

```text
03_bash_regex.md
```

For example:

```text
\d
```

belongs in fundamentals.

But:

```python
re.search(r"\d+", text)
```

belongs in the Python file.

---

## 4. Distinguish "introduced" from "completed"

Maintain this distinction throughout the course.

A concept may be:

```text
NOT INTRODUCED
INTRODUCED
PRACTICED
UNDERSTOOD
DOCUMENTED
COMPLETED
```

Do not assume that because a concept appears in the notes that
the user has mastered it.

---

# Progress Tracking

The assistant maintains the progress assessment. The user should not
have to calculate percentages or ETAs manually.

After each significant lesson is completed, the assistant should give
the user an exact replacement `# Current Progress

## Status

**Current Phase:** Phase 1 — Regex Fundamentals

**Current Lesson:** Phase 1 completed

**Lesson Status:** ✅ Complete

**Completed Phase 1 Milestones:** 18 / 18

**Phase 1 Progress:** 100%

**Overall Project Progress:** ~35%

**Estimated Remaining Time:** ~3–4.5 focused hours

**Last Updated:** 2026-08-11

---

## Progress by Phase

| Phase | Status | Progress | Estimated Remaining |
|---|---|---:|---:|
| Phase 1 — Regex Fundamentals | ✅ Complete | 100% | 0 min |
| Phase 2 — Groups & Extraction | 🟡 Next | 0% | ~30–45 min |
| Phase 3 — Python Regex | ⬜ Not Started | 0% | ~60–90 min |
| Phase 4 — Shell Regex | ⬜ Not Started | 0% | ~60–90 min |
| Phase 5 — Advanced Practical Regex | ⬜ Not Started | 0% | ~30–45 min |
| Phase 6 — Regex Engineering | ⬜ Not Started | 0% | ~30–45 min |

---

## Phase 1 — Completed Concepts

- [x] Regex mental model
- [x] Literal characters
- [x] Dot `.`
- [x] Character classes `[]`
- [x] Character ranges
- [x] Negated character classes `[^]`
- [x] `\d`, `\D`
- [x] `\w`, `\W`
- [x] `\s`, `\S`
- [x] Anchors `^`, `$`, `\A`, `\Z`
- [x] Basic quantifiers `+`, `*`, `?`
- [x] Exact/range quantifiers `{n}`, `{n,}`, `{n,m}`
- [x] Grouping `(...)`
- [x] Alternation `|`
- [x] Character class vs alternation
- [x] Word boundary `\b`
- [x] Escaping
- [x] Python raw-string concept
- [x] Matching vs searching
- [x] Greedy quantifiers
- [x] Lazy quantifiers

---

## Introduced but Not Yet Completed

- [ ] Capturing groups
- [ ] Non-capturing groups
- [ ] Named groups
- [ ] Backreferences
- [ ] Lookarounds
- [ ] Python `re` API
- [ ] Match objects
- [ ] Python flags in practice
- [ ] grep
- [ ] grep -E
- [ ] Bash `=~`
- [ ] sed
- [ ] awk
- [ ] Regex dialect differences
- [ ] Advanced regex engineering

---

## Immediate Next Step

Start Phase 2 — Groups & Extraction.

First topic:

**Capturing Groups**

Begin with:

```
(\d{3})-(\d{4})
```

---

## Current Repository State

`01_regex_fundamentals.md` currently contains the material the user
has actually documented so far.

The file should be treated as the source of truth for documented
fundamentals.

Do not assume that a concept is completed merely because it appears
in this README or in the curriculum.

When the user provides an updated `01_regex_fundamentals.md`, inspect
that actual file before deciding what has already been documented.

---

# Fresh Chat Master Prompt

Use this prompt when starting a completely new chat.

---

I am continuing a long-term Regular Expression study project.

I have attached/shared the repository files, especially:

* README.md
* 01_regex_fundamentals.md
* 02_python_regex.md
* 03_bash_regex.md
* 04_test_data.txt
* 05_exercises.md

Read README.md first.

README.md is the authoritative study plan and describes the teaching
method, repository structure, current progress, and curriculum.

My goal is to understand regex deeply enough for practical Python and
shell scripting work, at approximately the level expected from an
experienced IT professional.

Do NOT teach this as a giant beginner tutorial.

Teach interactively.

The learning loop should be:

```
concept
  ↓
explanation
  ↓
examples
  ↓
exercises
  ↓
my answers
  ↓
correction
  ↓
exact Markdown content to add
  ↓
next concept
```

Important rules:

1. Do not jump ahead.
2. Do not assume I understand something merely because it appeared
   in the Markdown.
3. Distinguish between "introduced", "practiced", "understood",
   and "completed".
4. If something was only mentioned but not practiced, return to it.
5. Preserve the existing Markdown rather than rewriting it.
6. When adding notes, give me exact Markdown blocks to copy-paste.
7. Keep fundamentals, Python-specific material, and Bash-specific
   material in their respective files.
8. Do not make the explanation unnecessarily verbose.
9. Prefer reasoning and pattern construction over memorizing symbols.
10. Correct terminology when necessary, but don't derail the lesson
    for minor wording issues.
11. Use realistic examples and exercises.
12. Do not introduce advanced regex features before the fundamentals
    are solid.
13. When the user asks for a Markdown file because copying response
    formatting is inconvenient, create the actual `.md` file and
    provide it as a downloadable file.
14. After each significant completed lesson, provide an exact updated
    `# Current Progress` section for README.md.
15. Include an ETA for the remaining course, but treat it as an
    estimate rather than a deadline.
16. Do not count a concept as completed until it has actually been
    practiced and demonstrated.

I will answer exercises myself. Do not give the solution before I
attempt them unless I explicitly ask.

Before teaching the next concept, determine from README.md and the
current Markdown what has actually been completed.

Continue from the exact point where we stopped.

---

# Continuation Prompt

Use this shorter prompt when continuing after an interruption.

---

Continue my Regex study project.

Read `README.md` first, then inspect the current Markdown files I have
provided.

Determine exactly what has been taught, practiced, documented, and
completed.

Do not assume that something is understood merely because it appears
in the Markdown.

Follow the teaching approach in README.md:

```
concept
  ↓
explanation
  ↓
examples
  ↓
exercises
  ↓
correction
  ↓
exact Markdown update
  ↓
next concept
```

Continue from the exact unfinished concept.

Do not jump ahead.

My goal is practical regex proficiency for Python and Bash/shell
scripting at an experienced IT level, not regex specialization.

If a concept was previously introduced but not properly practiced,
practice it before moving forward.

After completing a significant lesson, provide an exact replacement
`# Current Progress` section for README.md, including the updated
ETA.

If I ask for a Markdown file because copying response formatting is
difficult, create the actual `.md` file and provide it as a download.

---

# Important State-Tracking Rule

When a new chat starts, the assistant should NOT rely solely on
conversation memory.

The repository is the source of truth.

The assistant should inspect:

1. `README.md`
2. `01_regex_fundamentals.md`
3. `02_python_regex.md`
4. `03_bash_regex.md`
5. `05_exercises.md`

and determine the actual state from those files.

---

# End Goal

By the end of this project, I should be able to:

* read regex naturally
* construct regex from English requirements
* explain regex behavior precisely
* validate strings
* search text
* extract data
* replace data
* use Python's `re` module confidently
* use grep and grep -E confidently
* use Bash `=~`
* understand shell globbing vs regex
* understand basic sed/awk regex usage
* recognize common advanced regex constructs
* understand Python vs POSIX/ERE differences
* debug regex failures
* recognize when regex is the wrong tool

The goal is strong practical engineering knowledge, not regex trivia.

---

## One final thing

I would **not start a new chat quite yet** if this conversation is still working. We can continue here.

But from now on, the `README.md` above gives us a **checkpoint mechanism**. If the context gets unwieldy, start a new conversation, upload:

```text
README.md
01_regex_fundamentals.md
02_python_regex.md
03_bash_regex.md
05_exercises.md
````

and use the **Continuation Prompt**.