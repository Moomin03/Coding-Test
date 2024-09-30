import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    up, down = 1, 1
    for i in range(M, M-N, -1):
        up *= i
    for j in range(N, 1, -1):
        down *= j
    print(int(up/down))