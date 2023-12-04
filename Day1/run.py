nums = "1234567890"
numWords = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9","zero":"0"}

def contains_number(string):
    for char in string:
        if char.isdigit():
            return True
    return False

def valRight(data, line, i):
    for j in range(0, len(data[i])):
        if line[j] in nums:
            return line[j]
        else:
            for word in numWords:
                if word in line[j:j+len(word)]:
                    return numWords.get(word)

def valLeft(data, line, i):
    for j in range(len(data[i])-1, -1, -1):
        if line[j] in nums:
            return line[j]
        else:
            for word in numWords:
                if word in line[j-len(word)+1:j+1]:
                    return numWords.get(word)
def dothis(fileName):
    total = 0
    with open(fileName, "r") as file:
        data = file.readlines()
        for i in range(0,len(data)):
            curr = ""
            line = data[i]
            curr += valRight(data, line, i)
            curr += valLeft(data, line, i)

            print(curr)
            total += int(curr)
    return total



if __name__ == "__main__":
    dep = dothis('2023\Day1\input.txt')

    print(dep)