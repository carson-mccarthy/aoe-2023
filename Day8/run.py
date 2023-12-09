import functools
import math

def getSteps(ins,c,steps):
    step = 0
    while True:
        for i in ins:
            c = steps[c][i]
            step +=1
            if c[2] == "Z":
                return step

def dothis1(lines):
    #ins = "LR"
    ins = "LLRLRRRLLRRRLRRLRRLRLRRRLRRRLRLLRLRRLRRLRLLRRLRRRLRRLRLRLRLRRRLRRLRLLLRRLRRRLLLRLRRRLRRRLLRRLRRRLRLRRRLLLRRLLRRLRRLLLRRRLRRRLRRRLRRLLRLRLRLRRRLRLRLRRLRRLRLRRRLRRLRRRLRRRLLLRLRRLRRLRLLRRLLRRLRRLLRLRRLRRLRLRLLLRLLRRLRRLRRRLLRRLLRRRLRRLRRRLRRRLLRRRLRRRLLRRRLRLRLLRRLRLRLRRRR"
    steps = {}
    for l in lines:
        dat = l.strip().split("=")
        data = dat[1][2:10].split(",")
        steps[dat[0].strip()] = {"L":data[0].strip(), "R":data[1].strip()}
    step = 0
    currs = []
    for ste in steps.keys():
        if ste[2] == "A":
            currs.append(ste)
    print(currs)
    currTimes = {}
    for c in currs:
        currTimes[c] = getSteps(ins,c,steps)
        
    print(currTimes)
    return math.lcm(19241, 18157, 19783, 16531, 21409, 14363)


if __name__ == "__main__":
    f = open('2023\Day8\input.txt', "r")
    dep = dothis1(f.readlines())
    print(dep)