import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
con = [True for i in range(b+1)]
con[0], con[1] = False, False
for i in range(2, b+1):
    if con[i]:
        for j in range(2*i, b+1, i):
            con[j]=False
sosu = [i for i in range(b+1) if con[i]]
con_sosu = [i for i in sosu if i>=a and i<=b]
if len(con_sosu)!=0:    
    print(sum(con_sosu))
    print(con_sosu[0])
else:
    print(-1)