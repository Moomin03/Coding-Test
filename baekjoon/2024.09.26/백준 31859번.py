import sys
b, a = list(map(str, sys.stdin.readline().strip().split()))
b = int(b)
alpha = []
discard = []
for i in a:
    if i not in alpha:
        alpha.append(i)
    else:
        discard.append(i)
alpha = ''.join(alpha)+str(len(discard)+4)
alpha = str(b+1906)+alpha
alpha = ''.join(list(alpha)[::-1])
alpha = 'smupc_'+alpha
print(alpha)