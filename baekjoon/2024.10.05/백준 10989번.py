import sys

# 입력받을 수의 개수
a = int(sys.stdin.readline())

# 수의 범위가 0 ~ 10,000 이므로, 0부터 10,000까지 저장할 배열 생성
max_value = 10000
count = [0] * (max_value + 1)

# 숫자 입력을 받아서 카운팅 배열에 저장
for _ in range(a):
    num = int(sys.stdin.readline())
    count[num] += 1

# 카운팅 배열을 이용해 정렬된 결과 출력
for num in range(max_value + 1):
    if count[num] > 0:
        for _ in range(count[num]):
            print(num)
