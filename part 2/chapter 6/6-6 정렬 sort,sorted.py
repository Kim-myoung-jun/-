# 6-6 정렬 sort,sorted

arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print("sorted(arr1) - ", sorted(arr1))
print("arr1 - ", arr1)
#result1 = sorted(arr1)
#print(result1)

arr2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print("arr2.sort() - ", arr2.sort())
print("arr2 - ", arr2)
#arr2.sort()
#print(arr2)

arr3 = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]
result3 = sorted(arr3, key=setting)
print(result3)