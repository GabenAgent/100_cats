with open("going_to_the_river.txt", "r") as file:
    monologue = file.read()

content_upper = monologue.upper()

with open("going_to_the_river_2.txt", "w") as file_2:
    file_2.write(content_upper)
