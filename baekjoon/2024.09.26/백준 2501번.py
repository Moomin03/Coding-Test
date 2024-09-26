try:
    yaksu = []
    a, b = list(map(int, input().split()))
    for i in range(1, a+1):
        if a%i==0:
            yaksu.append(i)
    print(yaksu[b-1])
except IndexError:
    print(0)