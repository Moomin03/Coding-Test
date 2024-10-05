list1 = []
for i in range(5):
    list1.append(list(input()))
max_len = 0
for i in list1:
    max_len = max(max_len, len(i))
for i in list1:
    if len(i)!=max_len:
        for j in range(max_len-len(i)):
            i.append('NAN')
for i in range(max_len):
    for j in range(5):
        if list1[j][i]=='NAN':
            continue
        print(list1[j][i], end='')