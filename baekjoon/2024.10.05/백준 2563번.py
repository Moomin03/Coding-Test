import sys
dohwa = [[0 for _ in range(100)] for i in range(100)]
n_iter = int(sys.stdin.readline())
for _ in range(n_iter):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(b-1, b+9):
        for j in range(a-1, a+9):
            dohwa[i][j] = 1
result = 0
for i in dohwa:
    result += i.count(1)
print(result)