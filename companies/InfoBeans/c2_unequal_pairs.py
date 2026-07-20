def unequal_pairs(lst1: list, lst2: list) -> list:
    return [(i, j) for i in lst1 for j in lst2 if i != j]

print(unequal_pairs([1, 2, 3], [3, 1, 4]))