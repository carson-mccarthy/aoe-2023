import functools
import math

def dothis1(lines):
    sum = 0
    newMap = []
    gals = []
    for i, l in enumerate(lines):
        newMap.append(l.strip())
        if not '#' in l:
            newMap.append(l.strip())

    def transpose(matrix):
        # Transpose the matrix
        transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        # Convert each row to a string
        string_rows = [''.join(map(str, row)) for row in transposed]
        return string_rows
    tmp = transpose(newMap)
    newNewMap = []
    for i, l in enumerate(tmp):
        newNewMap.append(l)
        if not '#' in l:
            newMap.append(l.strip())

    newMap = transpose(newNewMap)
    for i, l in enumerate(newMap):
        for j, c in enumerate(l):
                if c == '#':
                    gals.append((i,j))
    for i in range(0,len(gals)):
         for j in range(i,len(gals)):
            sum += abs(gals[i][0]-gals[j][0]) + abs(gals[i][1]-gals[j][1])
    print(len(gals))
    return sum

def dothis1(lines):
    sum = 0
    newMap = []
    gals = []
    xChanges = [0]
    currX = 0
    yChanges = []
    currY = 0
    for i, l in enumerate(lines):
        if not '#' in l:
            currX+=1
        newMap.append(l.strip())
        xChanges.append(currX)

    def transpose(matrix):
        transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        # Convert each row to a string
        string_rows = [''.join(map(str, row)) for row in transposed]
        return string_rows
    tmp = transpose(newMap)
    for i, l in enumerate(tmp):
        if not '#' in l:
            currY +=1
        yChanges.append(currY)

    for i, l in enumerate(lines):
        for j, c in enumerate(l):
                if c == '#':
                    gals.append((i,j))
    newGals = []
    for g in gals:
        newGals.append((g[0]+xChanges[g[0]]*999999,g[1]+yChanges[g[1]]*999999))

    for i in range(0,len(newGals)):
         for j in range(i,len(newGals)):
            sum += abs(newGals[i][0]-newGals[j][0]) + abs(newGals[i][1]-newGals[j][1])
    print(len(newGals))
    return sum

if __name__ == "__main__":
    f = open('2023\Day11\input.txt', "r")
    dep = dothis1(f.readlines())
    #dep2 = dothis2(f.readlines())
    print("Part 1",dep)
    #print("Part 2",dep2)