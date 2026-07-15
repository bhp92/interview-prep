# Combination Sum — find all combinations that sum to target
# Same element can be reused unlimited times (hence "infinite combinations" feel)
# Approach: backtracking / recursion

def combination_sum(candidates: list, target: int) -> list:
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(list(current))
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i, not i+1 — allows reuse
            current.pop()  # unchoose

    backtrack(0, [], target)
    return result


# Test cases
print(combination_sum([2, 3, 6, 7], 7))   # [[2,2,3], [7]]
print(combination_sum([2, 3, 5], 8))       # [[2,2,2,2], [2,3,3], [3,5]]
print(combination_sum([2], 1))             # []