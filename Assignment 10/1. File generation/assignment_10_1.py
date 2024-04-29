import random
import os


def clear_file():
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        filename = i + ".txt"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File {filename} destroyed")


def generate_file():
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        filename = i + ".txt"
        with open(filename, "a") as file:
            random_digit = random.randint(1,100)
            file.write(str(random_digit))
            print(f"Generated {filename}, filled with {random_digit}")


def summary_file():
    with open("summary.txt", "w") as summ:
        for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            filename = i + ".txt"
            with open(filename, "r") as file:
                filler = file.readline()
                summ.write(f"{filename}: {filler}; ")
                print(f"Add {filename} and {filler} to summary")


clear_file()
generate_file()
summary_file()
