import sys
from itertools import combinations
a = []

while True:
    a.append(list(map(int, sys.stdin.readline().split())))
    if [0] in a:
        a.pop()
        break
for j in range(len(a)):
    for i in combinations(a[j][1:], 6):
        print(*i)
    print()
