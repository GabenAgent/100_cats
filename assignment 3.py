# print(False == (not True))
# print((True and False) == (True and False))
# print(not (True and "A" == "B"))

# user_input = int(input("The positive number is: "))
# for i in range(1, user_input +1):
#     if user_input % i == 0:
#         print(i)

# string = "aaaabchjjjjjswwwwwwwxyzaaaaaa"
# max_letter = ''  # a, b, c, h, j, s, w
# max_letter_len = 0  # 4, 1, 1, 1, 5, 1, 7
# letter = ''  # a, b, c, h, j, s, w
# length = 0  # 4, 1, 1, 1, 5, 1, 7
# for i in string:
#     if i == letter:
#         length += 1
#     else:
#         letter = i
#         length = 1
#     if length > max_letter_len:
#         max_letter = letter
#         max_letter_len = length
# print(max_letter)
#
# counter = 0
# x = ""
# for i in range(len(string)):
#     letter_count = string.count(string[i])
#     if letter_count > counter:
#         counter = letter_count
#         x = string[i]
# print(x)

# chess_board = 0
# one_piece = 0.065/1000000
# for i in range(64):
#     chess_board += one_piece
#     one_piece *= 2
# print(chess_board)

# user_1 = int(input("Сторона а = "))
# user_2 = int(input("Сторона b = "))
# user_3 = int(input("Сторона c = "))
# if user_1 == user_2 == user_3:
#     print("Равносторонний треугольник")
# elif user_1 != user_2 and user_2 != user_3 and user_1 != user_3:
#     print("Разносторонний треугольник")
# elif user_1 == user_2 or user_2 == user_3 or user_1 == user_3:
#     print("Равнобедренный треугольник")
