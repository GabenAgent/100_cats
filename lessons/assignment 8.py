# 100 cats solution:
from collections import Counter


def cats_solution(cats, rounds):
    cats_list = []
    for i in range(1, rounds + 1):
        for j in range(1, cats + 1):
            if j % i == 0:
                cats_list.append(j)
    print(cats_list)

    cats_count = Counter(cats_list)
    print(cats_count)
    cats_with_hats = {}
    for key, value in cats_count.items():
        if value % 2 != 0:
            cats_with_hats[key] = None

    return print(list(cats_with_hats.keys()))


cats_solution(100, 100)
