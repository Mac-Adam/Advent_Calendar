import re
def main():
    pattern = re.compile(r"(\d+)\s+(\d+)")
    arr1 = []
    arr2 = []
    with open("./in1.txt") as f:
         for line in f:
            line = line.strip()
            match = pattern.match(line)
            if match:
                val_a, val_b = match.groups()
                arr1.append(int(val_a))
                arr2.append(int(val_b))
            else:
                print(f"Skipping line: {line}")

if __name__ == "__main__":
    main()