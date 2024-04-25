def compute_difference(first: list, second: list) -> tuple:
    first_minus_second = [item for item in first if item not in second]
    second_minus_first = [item for item in second if item not in first]
    return first_minus_second, second_minus_first


result = compute_difference(['a', 'b', 'e'], ['c', 'c', 'd'])
print(result)


