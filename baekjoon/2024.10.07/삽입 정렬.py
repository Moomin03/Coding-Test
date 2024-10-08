'''
2. 삽입 정렬
 - 아이디어 : 처음부터 끝까지 키 값을 받아서 순회하는데, 
'''

array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(array)
for i in range(1, n):
    key = array[i]
    j = i-1
    while j >= 0 and array[j] > key:
        array[j+1] = array[j]
        print(array)
        j-=1
    array[j+1] = key
        
print(array)