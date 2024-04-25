# sentence = "Гаррі Поттер (англ. Harry Potter) — серія з семи фантастичних романів англійської письменниці..."
# counter = 0
# for i in sentence.split():
#     if i.isalnum():
#         counter += 1
# print(counter)

# sentence_1 = sentence.replace("—", " ")
# count_words = len(sentence_1.split())
# check = count_words == 12
# print(check)
# print(count_words == 12)

# start_string = "snake_case_text"
# a = start_string.title()
# end_string = a.replace("_", "")
# print(end_string)
# end_string_1 = start_string.title().replace("_", "")
# print(end_string_1)

# start_string = "SnakeCaseText"
# space = ""
# for i in start_string:
#     if i.isupper():
#         space += "_" + i.lower()
#     else:
#         space += i
# end_string = space
# print(end_string)
# end_string_1 = space.lstrip("_")
# print(end_string_1)
#
# start_string = "VeeeryLoooooongStriiiiiiing"
# space = ""
# for i in start_string:
#     if i.isupper():
#         space += "_" + i.lower()
#     else:
#         space += i
# end_string = space
# print(end_string)
# end_string_1 = space.lstrip("_")
# print(end_string_1)

# user_input = int(input("Give me a number: "))
# for i in range(1, user_input + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     print(i)

# user_input_1 = str(input())
# user_input_2 = str(input())
# if sorted(user_input_1) == sorted(user_input_2):
#     print("Oh shit, they are anagrams")
# else:
#     print("Shit happens, they are not anagrams")

# def triangle_area(x1, y1, x2, y2, x3, y3):
#     return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
#
#
# print(triangle_area(2, 1, 3, 4, 5, 6))
