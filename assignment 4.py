# def find_primes(a, b):
#     for i in range(a, b + 1):  # 1, 10
#         counter = 0
#         if i == 1:
#             continue
#         for q in range(1, i + 1):
#             # 1, 2, 3, 4, ..., 100
#             if i % q == 0 and i != q and q != 1:
#                 counter += 1
#         if counter == 0:
#             print(i)
#
#
# find_primes(1, 100)

# def unique_characters(s):
#     for i in range(len(s)):
#         letter_count = s.count(s[i])
#         if letter_count > 1:
#             return False
#     return True
#
#
# # reference to homework #3 where I counted (a) instead of (w) :)))
# # although I googled that there is such a thing as (set), which greatly simplifies this task
# print(unique_characters("qwerty"))

# def swap(string):
#     swapped_string = ""
#     for letter in string:
#         if letter.isupper():
#             swapped_string += letter.lower()
#             print(swapped_string)
#         elif letter.islower():
#             swapped_string += letter.upper()
#             print(swapped_string)
#         else:
#             swapped_string += letter
#             print(swapped_string)
#     return swapped_string
#
#
# print(swap('HelLo!'))

# def fibonacci(n):
#     first = 1  # 1, 2, 3, 5...
#     second = 1  # 2, 3, 5, 8...
#     for i in range(n-1):
#         first, second = second, first + second
#         print(first, second)
#     return first
#
#
# print(fibonacci(10))

# def simple_interest(initial_amount, interest_rate, years):
#     for i in range(years):
#         interest_calculate = initial_amount * interest_rate
#         initial_amount += interest_calculate
#     return round(initial_amount, 2)
#
#
# print(simple_interest(10000, 0.1, 10))

# def password_strength(s):
#     points = 0
#     char_count = len(s)
#     points += char_count
#     unique_lower = set()
#     unique_digit = set()
#     unique_special = set()
#     for i in s:
#         if i.islower():
#             unique_lower.add(i)
#     points += len(unique_lower) * 2
#     unique_upper = set()
#     for i in s:
#         if i.isupper():
#             unique_upper.add(i)
#     points += len(unique_upper) * 3
#     for i in s:
#         if i.isdigit():
#             unique_digit.add(i)
#     points += len(unique_digit) * 4
#     for i in s:
#         unique_special.add(i)
#     points += len(unique_special) * 5
#     return points
#
#
# password = input("Enter your password: ")
# print(password_strength(password))
