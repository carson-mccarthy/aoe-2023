import functools
import math

def dothis1(lines):
    sum = 0
    
    def getNextVal(values):
        vals = [int(float(value)) for value in values]
        tmp = []
        tmp.append(vals)
        run = True
        while run:
            for k, v in enumerate(tmp):
                t = []
                for j in range(0, len(v)-1):
                    t.append(int(v[j+1])-int(v[j]))
                tmp.append(t)
                if all(value == 0 for value in tmp[k+1]):
                    tmp[k+1].append(0)
                    run = False
                    break
        le = len(tmp) - 1
        ret = [0]
        for i, v in enumerate(reversed(tmp)):
            if all(value == 0 for value in v):
                continue
            else:
                ret.append(v[-1] + ret[i-1])
        return ret[-1]

    vals = []
    for l in lines:
        dat = l.strip().split()
        sum += getNextVal(dat)
    return sum

def dothis2(lines):
    sum = 0
    
    def getNextVal(values):
        vals = [int(float(value)) for value in values]
        tmp = []
        tmp.append(vals)
        run = True
        while run:
            for k, v in enumerate(tmp):
                t = []
                for j in range(0, len(v)-1):
                    t.append(int(v[j+1])-int(v[j]))
                tmp.append(t)
                if all(value == 0 for value in tmp[k+1]):
                    tmp[k+1].append(0)
                    run = False
                    break
        le = len(tmp) - 1
        ret = [0]
        for i, v in enumerate(reversed(tmp)):
            if all(value == 0 for value in v):
                continue
            else:
                ret.append(v[0] - ret[i-1])
        return ret[-1]

    vals = []
    for l in lines:
        dat = l.strip().split()
        sum += getNextVal(dat)
    return sum


if __name__ == "__main__":
    f = open('2023\Day9\input.txt', "r")
    #dep = dothis1(f.readlines())
    dep2 = dothis2(f.readlines())
    #print("Part 1",dep)
    print("Part 2",dep2)