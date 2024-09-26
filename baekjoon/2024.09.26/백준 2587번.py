import sys
a = [int(sys.stdin.readline()) for _ in range(5)]
a.sort()
print(int(sum(a)/5))
print(a[len(a)//2])