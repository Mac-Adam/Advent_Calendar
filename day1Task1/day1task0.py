
with open("C:/Users/adams/Documents/GitHub/Advent_Calendar/day1Task1/data.txt", "r") as file:
    lines = file.readlines()
    elves = [0]

    for line in lines:
        if line == "\n":
            elves.append(0)
        else:
            elves[-1]+=int(line.strip("\n"))

    biggest = 3
    biggest2 =2
    biggest3 = 1
    for e in elves:
        if e >=biggest:
            biggest3 = biggest2
            biggest2 = biggest
            biggest = e
        elif e >=biggest2:
            biggest3 = biggest2
            biggest2 = e
        elif e >=biggest3:
            biggest3 = e

    print(biggest3+biggest2+biggest)