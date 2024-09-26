import math
import sys
a = int(sys.stdin.readline())
for _ in range(a):
    a, b = list(map(int, sys.stdin.readline().split()))    
    gcd = math.gcd(a, b)
    lcm = (a*b)//gcd
    print(lcm)