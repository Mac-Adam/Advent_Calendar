def draw (spritePos,pixelPos,line):
    if abs(spritePos-pixelPos)<=1:
        line[pixelPos] = "#"


def task2():
    with open("day10/data.txt") as file:
        with open("day10/output.txt","w") as output:
            lines =[["." for _ in range(40)]for _ in range(6)]

            register = 1
            cycle = 0

            for instruction in file:
                instruction = instruction.strip("\n")
                type = instruction.split(" ")[0]
                if type == "noop":
                    draw(register,cycle%40,lines[cycle//40])
                    cycle+=1
                    continue
                for _ in range(2):
                    draw(register,cycle%40,lines[cycle//40])
                    cycle+=1
                register += int(instruction.split(" ")[1])
            stringLines = []
            for line in lines:
                stringline = ""
                for c in line:
                    stringline+=c
                stringLines.append(stringline+"\n")
            output.writelines(stringLines)
            print("check output.txt for result")




def task1():
    with open("day10/data.txt") as file:
        sum = 0
        register = 1
        cycle = 1
        cycllesToLookAt = [20,60,100,140,180,220]
        for instruction in file:
            instruction = instruction.strip("\n")
            type = instruction.split(" ")[0]
            if type == "noop":
                if cycle in cycllesToLookAt:
                    print(f"stength: {register*cycle} register value: {register}")
                    sum += register*cycle
                cycle+=1
                continue
            for _ in range(2):
                if cycle in cycllesToLookAt:
                    print(f"stength: {register*cycle} register value: {register}")
                    sum += register*cycle
                cycle+=1
            register += int(instruction.split(" ")[1])
        print(cycle) 
        
        print(f"Task1: {sum}")

            


def main():
    task1()
    task2()


if __name__ == "__main__":
    main()