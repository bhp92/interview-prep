# Regular Expression

## 1. What is a Regular Expression?

A regular expression (regex) is a pattern language used to describe sequence of characters that we want to find, match, extract, validate or replace in text.

A regex is not the data itself. It is the description of what the desired data should look like.

### 1.1 Literal Characters

The simplest regex consists of literal characters.

Example:

```
    cat
```

matches the sequence of characters

```
    c → a → t
```

### 1.2 Dot `.`

The dot `.` matches any single character except a newline by default.

For example:

```
    c.t
```

can match:

```
    cat
    cot
    cut
    c9t
    c-t
```

The dot represents exactly one character.

Therefore:

```
    ct       → no match
    coat     → no match
```

The behavior of `.` can be changed by regex options such as DOTALL,
which is covered later.

### 1.3 Character Classes

Square brackets `[]` define a character class.

```
    [abc]
```

matches exactly one character that is either:

```
    a
    b
    c
```

A character class chooses one character from the characters listed
inside it.

For example:

```
    [abc]at
```

can match:

```
    aat
    bat
    cat
```

but not:

```
    dat
```

because `d` is not part of the character class.

### 1.4 Character Ranges

A hyphen `-` inside a character class can define a range.

```
    [a-z]
```

matches one lowercase English letter.

```
    [A-Z]
```

matches one uppercase English letter.

```
    [0-9]
```

matches one digit from 0 through 9.

Ranges can be combined:

```
    [a-zA-Z]
```

matches one English alphabetic character.

```
    [0-9a-zA-Z]
```

matches one ASCII letter or digit.

### 1.5 Negated Character Classes

A caret `^` immediately after `[` negates the character class.

```
    [^abc]
```

matches one character that is not `a`, `b`, or `c`.

Compare:

```
    [abc]
```

which means:

```
    one character that is a, b, or c
```

with:

```
    [^abc]
```

which means:

```
    one character that is not a, b, or c
```

The meaning of `^` therefore depends on its position.

At the beginning of a regex:

```
    ^
```

it is an anchor.

Immediately after `[`:

```
    [^abc]
```

it negates the character class.

### 1.6 Character Classes with Shorthand

Some commonly used character classes have shorthand forms.

```
    \d
```

matches a digit.

```
    \D
```

matches a non-digit.

```
    \w
```

matches a word character.

```
    \W
```

matches a non-word character.

```
    \s
```

matches a whitespace character.

```
    \S
```

matches a non-whitespace character.

These constructs match one character unless combined with a
quantifier.

For example:

```
    \d+
```

means one or more digits.

### 1.7 Anchors

Anchors match positions rather than characters.

#### `^` — Start

```
    ^
```

matches the beginning of the string, or the beginning of a line when
multiline mode is enabled.

For example:

```
    ^Hello
```

requires `Hello` to occur at the beginning.

#### `$` — End

```
    $
```

matches the end of the string, or the end of a line when multiline
mode is enabled.

For example:

```
    world$
```

requires `world` to occur at the end.

Together:

```
    ^[0-9]+$
```

means that the entire string must consist of one or more digits.

#### `\A` and `\Z`

```
    \A
```

matches the absolute beginning of the string.

```
    \Z
```

matches the absolute end of the string.

Unlike `^` and `$`, their behavior is not changed by multiline mode.

This distinction becomes important when working with multiline text
and Python regex flags.

## 2. Quantifiers

A quantifier specifies how many times the preceding regex element
may occur.

### `+` — one or more

```
    [0-9]+
```

Matches one or more digits.

```
    1
    123
    987654
```

At least one occurrence is required.

### `*` — zero or more

```
    [0-9]*
```

Matches zero or more digits.

The empty string is also allowed.

```
    ""
    1
    123
    987654
```

### `?` — zero or one

```
    [0-9]?
```

Matches zero or one digit.

### `{n}` — exactly n

```
    [0-9]{3}
```

Matches exactly three digits.

### `{n,}` — at least n

```
    [0-9]{3,}
```

Matches three or more digits.

### `{n,m}` — between n and m

```
    [0-9]{3,5}
```

Matches between three and five digits, inclusive.

Summary:

```
    +      1 or more
    *      0 or more
    ?      0 or 1
    {n}    exactly n
    {n,}   at least n
    {n,m}  between n and m
```

## 3. Grouping

Parentheses `()` group multiple regex elements and allow them to be
treated as a single unit.

For example:

```
    ab+
```

means:

```
    `a` followed by one or more `b` characters.
```

Whereas:

```
    (ab)+
```

means:

```
    one or more repetitions of the complete sequence `ab`.
```

Examples:

```
    ab
    abab
    ababab
```

The quantifier applies to the immediately preceding regex element or
group.

---

## 4. Alternation

The `|` character means OR.

```
    cat|dog
```

matches either:

```
    cat
    dog
```

Parentheses can be used to group alternatives:

```
    (cat|dog)
```

means:

```
    either `cat` or `dog` as one grouped pattern.
```

A quantifier can then operate on the entire group:

```
    (cat|dog)+
```

matches one or more repetitions of either `cat` or `dog`.

Examples:

```
    cat
    dog
    catdog
    dogcat
    catcat
```

### Character classes vs alternation

A character class chooses between individual characters:

```
    [abc]
```

means one character that is either `a`, `b`, or `c`.

Alternation chooses between complete patterns:

```
    (cat|dog)
```

means either the complete string `cat` or the complete string `dog`.

Therefore:

```
    [abc]       → one character
    (cat|dog)   → one of two complete patterns
```

## 5. Word Boundary

`\b` represents a word boundary.

A word boundary occurs at the boundary between a word character
(`\w`) and a non-word character (`\W`), or at the beginning/end
of the string.

For example:

```
    \bcat\b
```

matches `cat` as a complete word.

It can match:

```
    cat
    the cat is here
    cat!
    (cat)
```

But it does not match:

```
    catalog
    bobcat
    cat123
    123cat
```

Important distinction:

```
    ^cat$
```

means the entire string must be exactly `cat`.

```
    \bcat\b
```

means `cat` must occur as a complete word, but it can occur inside
a larger string.

Therefore:

```
    ^ $   → anchors for the beginning/end of the string or line
    \b    → word boundary
```

## 6. Escaping

The backslash `\` is used to give special meaning to some characters
or to remove the special meaning from regex metacharacters.

Examples of regex constructs using `\`:

```
    \d    digit
    \w    word character
    \s    whitespace
    \b    word boundary
```

Regex metacharacters can be escaped when their literal character is
required:

```
    \.    literal period
    \+    literal plus
    \?    literal question mark
    \(    literal opening parenthesis
    \)    literal closing parenthesis
    \[    literal opening bracket
    \]    literal closing bracket
    \\    literal backslash
```

Example:

```
    example\.com
```

matches:

```
    example.com
```

where the period is treated as a literal period rather than the `.`
regex metacharacter.

### Python raw strings

Python has its own string escaping rules, so regex patterns are
commonly written using raw strings:

```python
    r"\d+"
```

instead of:

```python
    "\\d+"
```

The raw string makes the regex pattern easier to read by preventing
Python from interpreting most backslash escapes before the regex
engine receives the pattern.

Conceptually:

```
    Python source
        ↓
    Python string processing
        ↓
    regex pattern
        ↓
    regex engine
```

## 7. Matching vs Searching

A regex pattern describes what can match, but how the pattern is
applied determines whether we are validating an entire string or
finding a matching portion inside text.

For example:

```
    [0-9]+
```

can find a sequence of digits inside:

```
    abc123xyz
```

The pattern does not require the entire string to consist of digits.

To require the entire string to contain only digits:

```
    ^[0-9]+$
```

The anchors require the pattern to extend from the beginning to the
end.

Therefore:

```
    [0-9]+
```

and:

```
    ^[0-9]+$
```

have different purposes.

The first can find a digit sequence inside larger text.

The second describes a complete string consisting only of digits.

The distinction between searching for a pattern and validating an
entire value is important when using regex in Python and shell tools.

## 8. Greedy and Lazy Quantifiers

Quantifiers such as `*`, `+`, and `{n,m}` are greedy by default.

A greedy quantifier attempts to match as many characters as possible
while still allowing the rest of the regex to match.

For example:

```
    <.*>
```

given:

```
    <a> hello <b>
```

can consume from the first `<` through the last `>` because `.*`
greedily consumes as much as possible.

A lazy quantifier attempts to match as few characters as possible.

Lazy versions are formed by adding `?` after the quantifier:

```
    *?
    +?
    ??
    {n,m}?
```

For example:

```
    <.*?>
```

will generally match the shortest possible sequence between `<` and
`>`.

Therefore:

```
    greedy → consume as much as possible
    lazy   → consume as little as possible
```

Greedy and lazy behavior becomes particularly important when working
with repeated patterns and extraction.

### `\A` and `\Z`

```
    \A
```

matches the absolute beginning of the string.

```
    \Z
```

matches the absolute end of the string.

Unlike ^ and $, \A and \Z always refer to the beginning and
end of the entire string and are not affected by multiline mode.

Therefore:

```
^ / $     → beginning/end of string or line, depending on mode

\A / \Z   → absolute beginning/end of the entire string
```

For a single-line string without multiline mode, these may appear to
behave the same:

```
^cat$
```

and:

```
\Acat\Z
```

With multiline text, the distinction becomes important.