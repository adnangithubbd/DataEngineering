import numpy as np

arr = np.array([1, 2, 3, 5, 7, 8])
#todo filter
last = arr % 2 == 0
print(arr[last])

newArra = []
for i in arr:
    if i % 2 == 0:
        newArra.append(True)
    else:
        newArra.append(False)

another = [item for item in arr if item % 2 == 0]


