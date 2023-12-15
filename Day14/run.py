import functools
import math


def dothis1(lines):

    def cycle(lines):
        for j, l in enumerate(lines):
            for i in range(0, len(l)):
                for k in range(i,0,-1):
                    if l[k] == "O" and l[k-1] == ".":
                        lines[j][k] = "."
                        lines[j][k-1] = "O"
        return lines
    sum = 0
    newLines = []
    lines = list(zip(*lines))
    for j, l in enumerate(lines):
        curr = []
        for c in l:
            curr.append(c)
        newLines.append(curr)
    seen = {}
    repeated = []
    repStart = 0
    for cyc in range(350):
        sum = 0
        newLines = cycle(newLines)
        newLines = [list(row) for row in zip(*newLines)][::-1]
        newLines = cycle(newLines)
        newLines = [list(row) for row in zip(*newLines)][::-1]
        newLines = cycle(newLines)
        newLines = [list(row) for row in zip(*newLines)][::-1]
        newLines = cycle(newLines)
        newLines = [list(row) for row in zip(*newLines)][::-1]
        tmpLines = tuple(zip(*newLines))
        for i, l in enumerate(tmpLines):
            for c in l:
                if c == "O":
                    sum+=len(l)-i
        if tmpLines in seen.keys() and (tmpLines, sum) not in repeated:
            repeated.append((tmpLines, sum))
            if len(repeated) == 1:
                repStart = cyc
        if tmpLines not in seen.keys():
            seen[tmpLines] = sum

    # 84 is where cycle starts
    # repeat every 93
    billIdx = (1000000000-repStart-1)%len(repeated)
    print("start",repStart)
    print("Billion Index in Repeated",billIdx)
    print("Cycle size", len(repeated))
    return repeated[billIdx][1]

if __name__ == "__main__":
    f = open('2023\Day14\input.txt', "r")
    dep = dothis1(f.readlines())
    print("Part 1",dep)

