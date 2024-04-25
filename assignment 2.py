# # Make all these expressions true.
# print(10>5)
# print(42!="42")
# print(3<=4)

# # Print the text in which there will be a quote with double quotes.
# quote='"путін хуйло"'
# print(quote)

# # Get a string from user input. Check if the string is a palindrome.
# user_input=str(input("Text: "))
# user_revers=(user_input[::-1])
# check=user_input==user_revers
# print(check)


# # The program receives the user's name and age from the input.
# # Then you need to display the name and age in one line in several ways:
# name=input("What's your name? ")
# age=input("How old are you? ")
# print("Your name is "+name+"." " You are "+age+" years old.")
# print("Your name is {}. You are {} years old.".format(name, age))
# print(f"Your name is {name}. You are {age} years old.")

# # Format string with proper built-in function.
# string_1 = "Animals  "
# lowercase=string_1.casefold()
# print(lowercase)

# string_2 = "  Badger"
# capitalize=string_2.capitalize()
# print(capitalize)

# string_3 = "   HoneyPot   "
# remove_1=string_3.lstrip()
# remove_2=string_3.rstrip()
# remove_3=string_3.strip()
# print(remove_1)
# print(remove_2)
# print(remove_3)

# string_1 = "Bear"
# string_2 = "bear"
# string_3 = "BEAR"
# string_4 = "bEar"
# check_1=string_1.startswith("Be")
# check_2=string_2.startswith("Be")
# check_3=string_3.startswith("Be")
# check_4=string_4.startswith("Be")
# print(check_1)
# print(check_2)
# print(check_3)
# print(check_4)

# form_2=string_2.title()
# check_form_2=form_2.startswith("Be")
# print(check_form_2)
#
# form_3=string_3.swapcase().title()
# check_form_3=form_3.startswith("Be")
# print(check_form_3)
#
# form_4=string_4.replace("bEar", "Bear")
# check_form_4=form_4.startswith("Be")
# print(check_form_4)

# # Find a secret message in the following text:
# secret = "X!xeXnxiXlX XtxeXrxcXeXsX Xax XsX`XtXIX"
# rev=secret[::-1]
# secret_1=rev.replace("X", "").replace("x", "")
# print(secret_1)
