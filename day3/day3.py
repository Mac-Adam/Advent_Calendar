def getPriority(char):
    if char.upper() == char:
        return ord(char) - ord("A") + 27
    else:
        return ord(char) - ord("a") + 1

def task1(lines):
    sum =0
    for line in lines:

        line = line.strip("\n")
        middleIdx = len(line)//2
        
        first = line[:middleIdx]
        second = line[middleIdx:]

        itemMaskFirst = set(first)
        itemMaskSecond = set(second)

        common = itemMaskFirst.intersection(itemMaskSecond)
        char = common.pop()
        sum+= getPriority(char)
    return sum
def task2(lines):
    sum =0
    for i in range(len(lines)//3):
        l1 = set(lines[3*i].strip("\n"))
        l2 = set(lines[3*i+1].strip("\n"))
        l3 = set(lines[3*i+2].strip("\n"))
        common = l1.intersection(l2).intersection(l3)
        sum+= getPriority(common.pop())
    return sum

with open("C:/Users/adams/Documents/GitHub/Advent_Calendar/day3/data.txt",'r') as file:
    lines = file.readlines()
    print(task1(lines))
    print(task2(lines))
        