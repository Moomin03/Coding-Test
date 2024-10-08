'''
3. 선택 정렬
 - 아이디어 : for문을 돌면서 가장 작은 값의 위치를 기억한다.
'''
array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
for i in range(len(array)-1):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
print(array)