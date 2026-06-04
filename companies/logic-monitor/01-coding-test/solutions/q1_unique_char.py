from collections import Counter

def first_unique_char(s: str) -> str:
    count = Counter(s.lower())
    for char in s:
        if count[char.lower()] == 1:
            return char
    return ''

for i in ['stress', 'sTreSS', 'moonmmen']:
    print(first_unique_char(i))