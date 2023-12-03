lookupDS={
        0:'0',
        1:'1',
        2:'2',
        3:'=',
        4:'-'
    }
lookupSD={
        '=':-2,
        '-':-1,
        '0':0,
        '1':1,
        '2':2
    }

def getNums(nums):
    with open("day25/data.txt","r")as file:
        for line in file:
            nums.append(line.strip('\n'))


def SNAFUToDec(num):
    
    dec = 0
    for idx,val in enumerate(num):
        pow = len(num)-idx-1
        dec+= lookupSD[val]*(5**pow)
    return dec

def decToSNAFUT(num):
    i = 0
 
    snafut = ''
    while num !=0:
        temp = num%5
        newS = lookupDS[temp]
        snafut = newS+snafut
        num -= lookupSD[newS]
        num//=5
        i+=1
    return snafut


def task1():
    nums = []
    getNums(nums)
    sum = 0
    for num in nums:
        sum+=SNAFUToDec(num)
    print(decToSNAFUT(sum))


if __name__ == "__main__":
    task1()