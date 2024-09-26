import math
import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
n_iter = int(math.sqrt(b))
con_list = [math.pow(i+1, 2) for i in range(n_iter) if pow(i+1, 2)>=a and pow(i+1, 2)<=b]
if len(con_list)!=0:    
    print(int(sum(con_list)))
    print(int(con_list[0]))
else:
    print(-1)