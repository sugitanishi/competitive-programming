import sys
sys.setrecursionlimit(10000000)
input=lambda : sys.stdin.readline().rstrip()

import math
print(2**(math.floor(math.log2(int(input())))+1)-1)