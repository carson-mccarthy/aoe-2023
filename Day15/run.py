import functools
import math


def dothis1(lines):
    sum = 0
    boxes = [[] for _ in range(256)]
    lines = lines.strip()
    def hasher(s):
        cv = 0
        for c in s:
            cv += ord(c)
            cv *= 17
            cv %= 256
        return cv
    
    for s in lines.split(","):
        label = ""
        fp = -1
        if "=" in s:
            label, fp = s.split("=")
            h = hasher(label)
            box = boxes[h]
            added = False
            for i, l in enumerate(box):
                if l[0] == label:
                    box[i] = (label, fp)
                    boxes[h] = box
                    added = True
                    break
            if not added:
                box.append((label, fp))
                boxes[h] = box
        else:
            label = s.split("-")[0]
            h = hasher(label)
            box = boxes[h]
            for i, l in enumerate(box):
                if l[0] == label:
                    box.pop(i)
                    boxes[h] = box
                    break
    for i, box in enumerate(boxes):
        for j, lense in enumerate(box):
            sum += (i+1) * (j+1) * int(lense[1])
    return sum

if __name__ == "__main__":
    f = open('2023\Day15\input.txt', "r")
    dep = dothis1(f.readline())
    #dep2 = dothis2(f.readlines())
    print("Part 1",dep)
    #print("Part 2",dep2)