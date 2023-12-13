import functools
import math
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.path import Path

def dothis1(lines):
    sz = 0
    lines = [line.strip() for line in lines]
    def doPipeConnect(p1, p1i, p1j, p2, p2i,p2j):
        if (p1 == 'S' or p2 == 'S') and not p1 == '.' and not p2 == '.':
            return True
        # same row
        if p1i == p2i:
            # p1 is right of p2
            if p1j > p2j:
                if p1 == '7' or p1 == 'J' or p1 == '-':
                    return p2 == 'L' or p2 == '-' or p2 == 'F'
                else:
                    return False
            # p1 is left of p2
            if p1j < p2j:
                if p1 == 'L' or p1 == '-' or p1 == 'F':
                    return p2 == '7' or p2 == 'J' or p2 == '-'
                else:
                    return False
        # same col
        else:
            # p1 is above p2
            if p1i < p2i:
                if p1 == '7' or p1 == 'F' or p1 == '|':
                    return p2 == 'L' or p2 == '|' or p2 == 'J'
                else:
                    return False
            # p1 is below p2
            if p1i > p2i:
                if p1 == 'L' or p1 == '|' or p1 == 'J':
                    return p2 == '7' or p2 == 'F' or p2 == '|'
                else:
                    return False

    def add_edges(graph, lines):
        for i, l in enumerate(lines):
            for j, c in enumerate(l):
                if j-1 >= 0 and doPipeConnect(lines[i][j],i,j,lines[i][j-1],i,j-1):
                    graph.add_edge((i, j), (i, j - 1))
                if j+1 < len(l) and doPipeConnect(lines[i][j],i,j,lines[i][j+1],i,j+1):
                    graph.add_edge((i, j), (i, j + 1))
                if i-1 >= 0 and doPipeConnect(lines[i][j],i,j,lines[i-1][j],i-1,j):
                    graph.add_edge((i, j), (i-1, j))
                if i+1 < len(lines) and doPipeConnect(lines[i][j],i,j,lines[i+1][j],i+1,j):
                    graph.add_edge((i, j), (i+1, j))

    G = nx.DiGraph()
    add_edges(G, lines)
    found = 0
    for i, l in enumerate(lines):
        for j, c in enumerate(l):
            if c == "S":
                print("FOUND S AT",i,j)
                found = (i,j)
    seen = [found]
    for s in seen:
        for node in G.neighbors(s):
            if not node in seen:
                seen.append(node)
    inside = 0
    for r in range(len(lines)):
        left = 0
        for c in range(len(lines[0])):
            if (r,c) not in seen and left % 2 == 1:
                inside += 1
            if lines[r][c] in ['|', 'L', 'J'] and (r,c) in seen:
                left += 1
    sz = (len(seen)/2)
    return sz, inside


if __name__ == "__main__":
    f = open('2023\Day10\input.txt', "r")
    dep = dothis1(f.readlines())
    #dep2 = dothis2(f.readlines())
    print("Part 1",dep)
    #print("Part 2",dep2)