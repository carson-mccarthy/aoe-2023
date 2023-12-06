# start soeed 0
# each whole mili +1 mm/ms

# Part 1
def dothis1(lines):
    ret = 0
    times = lines[0].split(":")[1].strip().split()
    distances = lines[1].split(":")[1].strip().split()
    
    def beatRace(time, dist):
        speed = 1
        wins = 0
        for i in range(1, time):
            if (time-i)*speed > dist:
                wins+=1
            speed+=1
        return wins
    win = 1
    for i in range(len(times)):
        win *= beatRace(int(times[i]),int(distances[i])) 
    return win


if __name__ == "__main__":
    f = open('2023\Day6\input.txt')
    lines = f.readlines()
    dep = dothis1(lines)
    print(dep)