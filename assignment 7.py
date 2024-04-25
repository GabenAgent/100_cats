# import random
#
# capitals = {
#         'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
#         'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa',
#         'Switzerland': 'Bern', 'Austria': 'Vienna',
#         'Belgium': 'Brussels',  'Sweden': 'Stockholm',
#         'Norway': 'Oslo', 'Denmark': 'Copenhagen',
#         'Finland': 'Helsinki', 'Poland': 'Warsaw',
#         'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'
# }
#
#
# def geography_quiz():
#
#     score = 0
#     life = 3
#
#     while True:
#         country = random.choice(list(capitals.keys()))
#         capital = capitals[country]
#         game = input(f"{name} your turn. What the capital of the {country}? "
#                      f"Type exit to quit the quiz :(").strip()
#         if game == "exit":
#             break
#         if game == capital:
#             score += 1
#             print(f"Good job {name}! Your score is {score}")
#         else:
#             hint1 = input(f"You are wrong! Here is a little hint: "
#                           f"The first letter is {capital[0]}. "
#                           f"What the capital of the {country}?")
#             if hint1 == capital:
#                 score += 1
#                 print(f"Good job {name}! Your score is {score}")
#             if hint1 != capital:
#                 hint2 = input(f"You are wrong again! Here is one more hint: "
#                               f"The second letter is {capital[1]}. "
#                               f"What the capital of the {country}?")
#                 if hint2 == capital:
#                     score += 1
#                     print(f"Good job {name}! Your score is {score}")
#                 if hint2 != capital:
#                     life -= 1
#                     print(f"Wrong! Life: {life}. X_x")
#                     if life == 0:
#                         print("You are ran out of lives. The game is over. GG WP :(")
#                         break
#
#     print(f"The final score for {name} is {score}! Gratz!")
#
#
# name = input("Please enter your name: ")
# geography_quiz()
#
#
# def majority_element(nums):
#     element = []
#     count = 0
#     for i in nums:
#         if count == 0:
#             element = i
#             count = 1
#         elif i == element:
#             count += 1
#         else:
#             count -= 1
#     print(element)
#     return element
#
#
# def test_majority_element():
#     result1 = majority_element([3, 2, 3])
#     assert result1 == 3
#
#     result1 = majority_element([2, 2, 1, 1, 1, 2, 2])
#     assert result1 == 2
#
#     result1 = majority_element([2, 2, 1, 1, 3, 3, 2, 2, 3])
#     assert result1 == 2
#
#
# test_majority_element()
#
#
# def get_subjects_not_passed_by_all_students(student_exams):
#     fail = set()
#     for item in student_exams.items():
#         name, score, subject = item
#         if score < 60:
#             fail.add(subject)
#     return fail
#
#
# def test_get_subjects_not_passed_by_all_students():
#     exams = [
#         ("Alice", 55, "Math"),
#         ("Bob", 40, "Math"),
#         ("Charlie", 30, "Math"),
#         ("Alice", 50, "Science"),
#         ("Bob", 45, "Science"),
#         ("Charlie", 40, "Science"),
#         ("Alice", 95, "History"),
#         ("Bob", 85, "History"),
#         ("Charlie", 90, "History"),
#     ]
#
#     assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}
#
# rome_dict = {
#     "I": 1, "V": 5, "X": 10,
#     "L": 50, "C": 100, "D": 500,
#     "M": 1000
# }
#
#
# def roman_to_int(s):
#     result = 0   # 1000 - 100 = 900 + 1000 = 1900 - 10 = 1890 + 100 = 1990 - 1 = 1989 + 5 = 1994
#     for i in range(len(s)):
#         if i + 1 < len(s):
#             if rome_dict[s[i]] < rome_dict[s[i + 1]]:
#                 result -= rome_dict[s[i]]
#             else:
#                 result += rome_dict[s[i]]
#         else:
#             result += rome_dict[s[i]]
#     return result
#
#
# def test_roman_to_int():
#      result1 = roman_to_int("III")
#      assert result1 == 3
#      result1 = roman_to_int("LVIII")
#      assert result1 == 58
#      result1 = roman_to_int("MCMXC IV")
#      assert result1 == 1994
#
#
# test_roman_to_int()
#
# roman_dict = {
#     1000: "M", 900: "CM", 500: "D", 400: "CD",
#     100: "C", 90: "XC", 50: "L", 40: "XL",
#     10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
# }
#
#
# def int_to_roman(s):
#     result = ""
#     for i in roman_dict:
#         while s >= i:
#             result += roman_dict[i]
#             s -= i
#     return result
#
#
# def test_int_to_roman():
#     result1 = int_to_roman(3)
#     assert result1 == "III"
#
#     result1 = int_to_roman(58)
#     assert result1 == "LVIII"
#
#     result1 = int_to_roman(1994)
#     assert result1 == "MCMXCIV"
#
#
# test_int_to_roman()
