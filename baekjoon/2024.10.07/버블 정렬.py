'''
1. 버블 정렬
 - 아이디어 : 인접한 두 요소를 비교해서 더 큰 값을 뒤로 보내는 방식으로 배열을 정렬
 - 시간복잡도 : O(n^2)
'''
array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(array)
for i in range(n):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
print(array)