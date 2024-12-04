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
    arr1.sort()
    arr2.sort()
    res = 0
    for (a,b) in zip(arr1,arr2):
        res += abs(a-b)
    
    num_of_occ = {}
    for num in arr2:
        if num in num_of_occ:
            num_of_occ[num] +=1
        else:
            num_of_occ[num] = 1
    res2 = 0
    for num in arr1:
        if num in num_of_occ:
            res2 += num*num_of_occ[num]

        
    print(res)
    print(res2)

if __name__ == "__main__":
    main()