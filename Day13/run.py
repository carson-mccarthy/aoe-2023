import functools
import math


def dothis1(lines):
    def canSmudge(s1, s2):
        miss = 0
        for i in range(0,len(s1)):
            if s1[i] != s2[i]:
                miss +=1
        return miss <= 1
    
    def getScore(r):
        seen = []
        for i, l in enumerate(r):
            hasSmudged = False
            seen.append(l)
            matchCount = 0
            checks = 0
            for j in range(0,len(seen)):
                if len(seen)+j >= len(r):
                    continue
                else:
                    checks+=1
                    if r[len(seen)+j] == seen[len(seen)-j-1]:
                        matchCount+=1
                    elif not hasSmudged and canSmudge(r[len(seen)+j], seen[len(seen)-j-1]):
                        matchCount+=1
                        hasSmudged = True
            if matchCount == checks and checks != 0 and hasSmudged:
                return len(seen)
    
    sum = 0
    reflections = []
    curr = []
    for l in lines:
        l = l.strip()
        if not l == "":
            curr.append(l)
        else:
            reflections.append(curr)
            curr = []
    reflections.append(curr)

    for k, r in enumerate(reflections):
        isMirror = False
        # check horizontal
        horScore = getScore(r)
        if horScore != 0 and not horScore == None:
            isMirror = True
            print(k, horScore)
            sum += horScore*100
        # check vertical if a mirror has not been found
        if isMirror:
            continue
        r = list(zip(*r))
        vertScore = getScore(r)
        if vertScore != 0:
            isMirror = True
            print(k, vertScore)
            sum += vertScore

    return sum

if __name__ == "__main__":
    f = open('2023\Day13\input.txt', "r")
    dep = dothis1(f.readlines())
    #dep2 = dothis2(f.readlines())
    print("Part 1",dep)
    #print("Part 2",dep2)