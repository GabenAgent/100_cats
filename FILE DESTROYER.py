import os


def clear_file():
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        filename = i + ".txt"
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File {filename} destroyed")


clear_file()