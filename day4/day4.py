def checkInclusion(first,second):
    first = [int(first[0]),int(first[1])]
    second = [int(second[0]),int(second[1])]

    if (first[0]<= second[0] and first[1] >= second[1]) or (first[0]>=second[0]and first[1]<=second[1]):
        return True
    else:
        return False
def checkOverlap(first,second):
    first = [int(first[0]),int(first[1])]
    second = [int(second[0]),int(second[1])]

    if((first[0]<= second[1] and first[0]>= second[1]) or (second[0]<=first[1]and second[0] >=first[1] )or (first[0] <= second[1] and first[1] >= second[1] ) or (second[0] <= first[1]and second[1]>=first[1])):
        return True
    else:
        return False


with open("day4/data.txt","r") as file:
    lines = file.readlines()
    inclusion = 0
    overlap = 0
    for line in lines:
        line = line.strip("\n")
        pairs = line.split(",")
        first = pairs[0].split("-")
        second = pairs[1].split("-")
        if(checkInclusion(first,second)):
            inclusion+=1
        if(checkOverlap(first,second)):
            overlap+=1
    print(inclusion)
    print(overlap)