def multiples_of_3(n: int) -> list:
    return [i for i in range(0, n, 3)]

for i in [10 , 20, 30]:
    print(multiples_of_3(i))
