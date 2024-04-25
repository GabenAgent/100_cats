# def user_info():
#     return int(input("Enter an integer: "))
#
#
# def check():
#     try:
#         user_input = user_info()
#         print("The integer you entered is: ", user_input)
#     except ValueError:
#         print("Try one more time!")
#         check()
#
#
# check()

# def user_info():
#     user_string = input("Enter a string: ")
#     user_integer = int(input("Enter an integer: "))
#     return user_string, user_integer
#
#
# def char_at_index():
#     user_string, user_integer = user_info()
#     try:
#         letter = user_string[user_integer]
#         print(f"Letter at index {user_integer} is {letter}")
#     except IndexError:
#         print("Index is out of range")
#         char_at_index()
#
#
# char_at_index()

# balance = 1000
#
#
# def transaction(amount, _type):
#     def deposit(amount):
#         global balance
#         balance += amount
#         print("New balance: ", balance)
#
#     def withdrawal(amount):
#         global balance
#         if balance >= amount:
#             balance -= amount
#             print("Withdrawal success. New balance: ", balance)
#         else:
#             print("No money - no honey, baby")
#
#     if _type == "deposit":
#         deposit(amount)
#     elif _type == "withdrawal":
#         withdrawal(amount)
#
#
# transaction(100, "withdrawal")

# import random
#
#
# def dice_roll():
#     return random.randrange(1, 7)
#
#
# rolls_1000 = [dice_roll() for i in range(1000)]
# print(rolls_1000)
# for j in range(1, 7):
#     count = rolls_1000.count(j)
#     print(f"Number {j}: {count} times")

# import random
# voters = 10000
#
#
# def receive_input():
#     region_input = int(input("Enter the number of regions: "))
#     rating = []
#     for i in range(region_input):
#         rating_input = int(input(f"Enter rating for candidate in region {i + 1}: "))
#         rating.append(rating_input)
#     return region_input, rating
#
#
# def simulate_region_election(sim):
#     regions = sim[0]
#     rating = sim[1]
#     candidates = ["candidate_1", "candidate_2"]
#     for i in range(regions):
#         vote = random.choices(candidates, weights=[rating[i], 100 - rating[i]], k=voters)
#         print("Region:", i + 1, "votes:", vote)
#
#     return sim
#
#
# simulate_region_election(receive_input())
