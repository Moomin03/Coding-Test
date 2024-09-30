import sys
n, k = map(int, sys.stdin.readline().split())
up = 1
down1, down2 = 1, 1
for i in range(1, n+1):
    up *= i
for i in range(1, k+1):
    down1 *= i
for i in range(1, (n-k)+1):
    down2 *= i
print(int(up/(down1*down2)))