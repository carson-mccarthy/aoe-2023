cards = [1] * 201

def checkScore(data):
    win, nums = data.split("|")
    ret = 0
    win = set(map(int, win.split()))
    nums = set(map(int, nums.split()))
    for num in nums:
        if num in win:
            ret +=1
    print(ret)
    return ret

def dothis(fileName):
    total = 0
    with open(fileName, "r") as file:
        data = file.readlines()
        for i, l in enumerate(data):
            l = l.strip()
            data = l.split(": ")[1]
            wins = checkScore(data)
            for j in range(i+1,i+wins+1):
                if j <= 200:
                    cards[j] += 1*cards[i]
            total += cards[i]
    return total



if __name__ == "__main__":
    dep = dothis('2023\Day4\input.txt')

    print(dep)