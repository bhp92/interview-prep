# Run-length expansion.
# Each character is repeated by the number that follows it; a character with no
# number after it appears once.
#   "A12B3CD4" -> "A"*12 + "B"*3 + "C"*1 + "D"*4
#
# Contract:
#   - any non-digit is a character; the digits after it are its repeat count
#   - a character with no digits after it defaults to a count of 1
#   - 0 is a valid count ("A0" -> ""), the character simply drops out
#   - a digit with no preceding character is malformed -> ValueError (fail fast,
#     rather than silently swallowing the number and returning a wrong answer)


def char_mul(s: str) -> str:
    i = 0
    parts = []
    while i < len(s):
        # Expect a character here. A leading/orphan digit has nothing to attach to.
        if s[i].isdigit():
            raise ValueError(f"number at index {i} has no preceding character")

        ch = s[i]
        i += 1

        # Collect the (possibly multi-digit) count that follows.
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1

        count = int(num) if num else 1
        parts.append(ch * count)

    return "".join(parts)


# Interview example
print(char_mul("A12B3CD4"))   # AAAAAAAAAAAABBBCDDDD

# Well-formed edge cases
print(char_mul("C"))          # C        -- no digit -> once
print(char_mul("AB"))         # AB       -- both default to once
print(char_mul("A10"))        # AAAAAAAAAA  -- multi-digit count
print(char_mul("A0B3"))       # BBB      -- zero count drops A
print(char_mul(""))           # (empty)

# Malformed input now fails loudly instead of returning a wrong answer
for bad in ["12A", "5"]:
    try:
        char_mul(bad)
    except ValueError as e:
        print(f"{bad!r} -> ValueError: {e}")