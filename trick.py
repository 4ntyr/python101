

import re 

def invalidID1(ID):
    return bool(re.fullmatch(r"(\d+)\1", str(ID))) # two identical halves

def invalidID2(ID):
    return bool(re.fullmatch(r"(\d+)\1+", str(ID))) # one or more repetitions of same substring

def solve2(filename):
    f = open(filename)
    sum1 = 0
    sum2 = 0
    for i1,i2 in [ [int(i) for i in b.split("-")] for b in f.read().split(",") ]:
        for i in range(i1,i2+1):
            if invalidID1(i):
                sum1 += i
            if invalidID2(i):
                sum2 += i
    return sum1,sum2

print(solve2("data.txt"))