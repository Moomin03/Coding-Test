import sys
con = [True for i in range(1000+1)]
con[0], con[1] = False, False
for i in range(2, 1000+1):
    if con[i]:
        for j in range(2*i, 1000+1, i):
            con[j]=False
sosu = [i for i in range(1000+1) if con[i]]
count = 0
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().strip().split()))
for i in b:
    if i in sosu:
        count += 1
print(count)