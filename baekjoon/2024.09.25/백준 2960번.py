import math
import sys
a, b = list(map(int, sys.stdin.readline().split())) # 찾고자 하는 b번째 지워진 값
con = [True for _ in range(a + 1)]
con[0], con[1] = False, False

# 지워진 값을 저장할 리스트
deleted = []

# 에라토스테네스의 체를 사용하여 소수 찾기
for i in range(2, a + 1):
    if con[i]:  # i가 소수인 경우
        deleted.append(i)  # 소수를 지운 목록에 추가
        for j in range(i * 2, a + 1, i):
            if con[j]:  # j가 아직 지워지지 않은 경우
                con[j] = False  # j를 지운다
                deleted.append(j)  # 지운 값을 목록에 추가
            
            # b번째 지워진 값 찾기
            if len(deleted) == b:
                print(deleted[-1])  # b번째로 지워진 값 출력
                break
    if len(deleted) >= b:
        break
