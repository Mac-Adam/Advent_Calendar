
def task1():
     with open("day9/data.txt") as file:
        for comand in file:
            direction = comand.split(" ")[0]
            steps = comand.split(" ")[1]


def main():
    task1()
   


if __name__ == "__main__":
    main()