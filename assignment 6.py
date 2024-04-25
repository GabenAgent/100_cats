# def compute_difference(first, second):
#     check_first = []
#     check_second = []
#     for i in first:
#         if i not in second:
#             check_first.append(i)
#     for i in second:
#         if i not in first:
#             check_second.append(i)
#     # for i in first:
#     #     if i in second:
#     #         if i not in check_first and i not in check_second:
#     #             check_first.append(i)
#
#     return check_first, check_second
#
# def compute_difference(first, second):
#     check_first = first.copy()
#     check_second = second.copy()
#     for i in first:
#         try:
#             check_second.remove(i)
#         except ValueError:
#             pass
#     for i in second:
#         try:
#             check_first.remove(i)
#         except ValueError:
#             pass
#
#     return check_first, check_second
#
#
# def test_compute_difference():
#     result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
#     print(result1)
#     assert result1 == (['a', 'b', 'c'], ['e'])
#
#     result2 = compute_difference([], ['c', 'd', 'e'])
#     print(result2)
#     assert result2 == ([], ['c', 'd', 'e'])
#
#     result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
#     print(result3)
#     assert result3 == ([1, 2, 3], [4, 4, 5, 6])
#
#     result4 = compute_difference([1, 2, 3], [2, 3, 4])
#     print(result4)
#     assert result4 == ([1], [4])
#
#
# test_compute_difference()
#
#
# def sum_of_two(nums, target):
#     for i in range(len(nums)):
#         term = target - nums[i]
#         for j in range(i + 1, len(nums)):
#             if nums[j] == term:
#                 return [i, j]
#
#     return []
#
#
# def test_sum_of_two():
#     result1 = sum_of_two([2, 7, 11, 15], 9)
#     assert result1 == [0, 1]
#
#     result2 = sum_of_two([3, 2, 4], 6)
#     assert result2 == [1, 2]
#
#     result3 = sum_of_two([3, 3], 6)
#     assert result3 == [0, 1]
#
#
# test_sum_of_two()
#
#
# def unique_elements(arr):
#     unique_list = []
#     for i in arr:
#         if arr.count(i) == 1:
#             unique_list.append(i)
#
#     return unique_list
#
#
# def test_unique_elements():
#     result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
#     assert result1 == [1, 3, 4]
#     result2 = unique_elements([1, 2, 3, 4, 5])
#     assert result2 == [1, 2, 3, 4, 5]
#     result3 = unique_elements([1, 1, 1, 1, 1])
#     assert result3 == []
#
#
# test_unique_elements()
#
#
# def odd_elements(arr):
#     odd_unique_list = []
#     for i in arr:
#         if arr.count(i) % 2 != 0 and i not in odd_unique_list:
#             odd_unique_list.append(i)
#
#     return odd_unique_list
#
#
# def test_odd_elements():
#
#     result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
#     assert result1 == [1, 3, 4]
#     result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
#     assert result1 == [1, 3, 4, 6]
#
#
# test_odd_elements()
