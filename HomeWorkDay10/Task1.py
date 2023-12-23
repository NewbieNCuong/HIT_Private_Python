import numpy as np

n = int(input())
# 1.
a = np.random.randint(1, 15, size = n)
print(a)
print(f"ndim: {a.ndim} \t shape: {a.shape} \t len: {len(a)} \t itemsize: {a.itemsize} \t dtype: {a.dtype}")
# 2. 
print("----------------------------------------------------------------")
b = np.arange(0, 200, 2)
print(b)
print(f"ndim: {b.ndim} \t shape: {b.shape} \t len: {len(b)} \t itemsize: {b.itemsize} \t dtype: {b.dtype}")
# 3.
print("----------------------------------------------------------------")
c = np.zeros((10, 10))
print(c)
print(f"ndim: {c.ndim} \t shape: {c.shape} \t len: {len(c)} \t itemsize: {c.itemsize} \t dtype: {c.dtype}")
# 4.
print("----------------------------------------------------------------")
d = np.eye(n)
print(d)
print(f"ndim: {d.ndim} \t shape: {d.shape} \t len: {len(d)} \t itemsize: {d.itemsize} \t dtype: {d.dtype}")
# 5.
print("----------------------------------------------------------------")
e = np.diag(a)
print(e)
print(f"ndim: {e.ndim} \t shape: {e.shape} \t len: {len(e)} \t itemsize: {e.itemsize} \t dtype: {e.dtype}")