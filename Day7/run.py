import functools
import math
# hand types go in highest to lowest
# function to get type of a hand
def getType(line):
    seen = {}
    jokeCount = 0
    for c in line:
        # if card is joker, add to joker count
        if c == 'J':
            jokeCount +=1
            continue
        # if card has been seen, increment seen count
        if c in seen:
            seen[c] = seen[c] + 1
        # else set to 1
        else:
            seen[c] = 1
    # increase all seen values by joker count, this enables the code
    # to handle jokers because we look for higher number of cards first, for example
    # when we have seen 2 types of cards, we check for 4 of a kind before full house
    # so even though we increment the number of cards "seen" over 5, it doesn't break the logic
    for s in seen:
        seen[s] = seen[s] + jokeCount
    if len(seen) == 0:
        return 0
    if len(seen) == 1:
        return 0 # 5 of a kind
    elif len(seen) == 2:
        if 4 in seen.values():
            return 1 # 4 of a kind
        else:
            return 2 # full house
    elif len(seen) == 3:
        if 3 in seen.values():
            return 3 # 3 of a kine
        elif 2 in seen.values():
            return 4 # two pair
        else:
            return 3
    elif len(seen) == 4:
        return 5 # pair
    else:
        return 6 # high

# compare method, just goes through each card in a hand and compares to the other, used for sorting
def comp(hand, currHand):
    letter_scores = {
        '2': 1, '3': 2, '4': 3, '5': 4, '6': 5,
        '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 0,
        'Q': 11, 'K': 12, 'A': 13
    }
    for i, card in enumerate(hand[0]):
        if letter_scores[card] > letter_scores[currHand[0][i]]:
            return -1
        elif letter_scores[card] < letter_scores[currHand[0][i]]:
            return 1
    return 0

def dothis1(lines):
    f = []
    fo = []
    fh = []
    tr = []
    tp = []
    p = []
    hc = []
    # keep track of hand types indiviually
    handTypes = [f,fo,fh,tr,tp,p,hc]
    hands = []
    sum = 0
    # for each hand
    for l in lines:
        l = l.strip()
        dat = l.split()
        # get the type and add to corresponding list
        t = getType(dat[0])
        handTypes[t].append(dat)
    # use custom comparator for sorting
    key_func = functools.cmp_to_key(comp)
    # for each hand type, sort
    for typ in handTypes:
        typ.sort(key=key_func)
        # and then add to the main list of hands
        for t in typ:
            hands.append(t)
    # for each hand, multiply bid by inverse pos (0 -> 1000, 1 -> 999, etc)
    for i, h in enumerate(hands):
        sum += int(h[1])*(1000-i)
    return sum
        



if __name__ == "__main__":
    f = open('2023\Day7\input.txt', "r")
    dep = dothis1(f.readlines())
    print(dep)