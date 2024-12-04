import re
def main():
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    inactive_instructions = re.compile(r"don't\(\).*?do\(\)")
    res1 = 0
    res2 = 0
    with open("./in3.txt") as f:
         for line in f:
            line = line.strip()
            match = mul_pattern.findall(line)
            for (a,b) in match:
                res1 += int(a)*int(b)
            line += 'do()'
            line = inactive_instructions.sub('', line)
            match = mul_pattern.findall(line)
            for (a,b) in match:
                res2 += int(a)*int(b)
    print(res1)
    print(res2)
if __name__ == "__main__":
    main()