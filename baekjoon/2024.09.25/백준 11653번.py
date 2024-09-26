import sys
import math
# 입력 받는 값
a = int(sys.stdin.readline())
# 에라토스테네스의 체
con = [True for i in range(a+1)]
con[0], con[1] = False, False
for i in range(2, int(math.sqrt(a))+1):
        if con[i]:
            for j in range(i*2, a+1, i):
                con[j]=False
# a보다 작은 소수 집합
con_data = [i for i in range(a+1) if con[i]]
# 소인수분해하기
count = 0
while a != 1:
    if a%con_data[count]==0:
        a//=con_data[count]
        print(con_data[count])
    else:
        count+=1