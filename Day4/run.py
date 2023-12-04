cards = [1] * 201

# Part 1
def checkScore1(data):
    win, nums = data.split("|")
    ret = 0
    win = set(map(int, win.split()))
    nums = set(map(int, nums.split()))
    for num in nums:
        if num in win:
            if ret == 0:
                ret = 1
            else:
                ret *=2
    return ret

def dothis1(fileName):
    total = 0
    with open(fileName, "r") as file:
        data = file.readlines()
        for l in data:
            l = l.strip()
            data = l.split(": ")[1]
            total += checkScore1(data)
    return total



# Part 2
def checkScore2(data):
    win, nums = data.split("|")
    ret = 0
    win = set(map(int, win.split()))
    nums = set(map(int, nums.split()))
    for num in nums:
        if num in win:
            ret +=1
    print(ret)
    return ret

def dothis2(fileName):
    total = 0
    with open(fileName, "r") as file:
        data = file.readlines()
        for i, l in enumerate(data):
            l = l.strip()
            data = l.split(": ")[1]
            wins = checkScore2(data)
            for j in range(i+1,i+wins+1):
                if j <= 200:
                    cards[j] += 1*cards[i]
            total += cards[i]
    return total



if __name__ == "__main__":
    dep = dothis2('2023\Day4\input.txt')

    print(dep)