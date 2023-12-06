stos = {}
stof = {}
ftow = {}
wtol = {}
ltot = {}
ttoh = {}
htol = {}
maps = [stos, stof, ftow, wtol, ltot, ttoh, htol]
stages = {0:"seed", 1:"soil",2:"fert",3:"water",4:"light",5:"temp",6:"hum",7:"loc"}
# Part 1
def convert(idx):
    for i in range(6, -1, -1):
        currMap = maps[i]
        for dest in currMap:
            source = int(currMap[dest][0])
            length = int(currMap[dest][1])
            dest = int(dest)
            if int(idx) >= dest and int(idx) < dest + length:
                idx = int(idx) + (source - dest)
                break
    return int(idx)

def findLowestSeed(seeds):
    location = 0
    while True:
        s = convert(location)
        for seed in seeds:
            if s > int(seed[0]) and s < int(seed[0])+int(seed[1]):
                return location
        location += 1
        if location % 100000 == 0:
            print(location)

def dothis1(fileName):
    total = 0
    seeds = []
    currMap = -1
    with open(fileName, "r") as file:
        data = file.readlines()
        for l in data:
            l = l.strip()
            if l == "":
                continue
            if "seeds: " in l:
                nums = l.split(":")[1].split()
                pairs = [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]
            elif l[0].isalpha():
                currMap+=1
                print(l + " : " + str(currMap))
            else:
                d = l.split()
                maps[currMap][d[0]] = (d[1], d[2])
    return findLowestSeed(pairs)



if __name__ == "__main__":
    dep = dothis1('2023\Day5\input.txt')
    print(dep)