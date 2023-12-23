import numpy as np

# 1. uniform sinh ra số thực, còn randint sinh ra số nguyên
arr = np.random.uniform(0, 11, size = (3, 20))
print(arr)
# 2
print(f"Vi tri max: {np.argmax(arr)}")
print(f"Vi tri min: {np.argmin(arr)}")
# 3: Có thể dùng flatten hoặc ravel, nhưng flatten trả về copy, còn ravel trả về view
arr = arr.ravel()
print(np.delete(arr, 0))
# 4.
arr = np.sort(arr, kind='quicksort')[::-1]
print(arr)
# 5. Nếu như kh sử dụng searchsorted thì sẽ dùng cách cho k vào rồi sắp xếp rồi in ra vị trí của k(Cách này có thể có số = k => k đc)
k = float(input("Nhap k: "))
# thêm dấu trừ ở đây quá perfect, muốn biết tại sao k =))
indexk = np.searchsorted(-arr, -k)
arr = np.insert(arr, indexk, k)
print(arr)


