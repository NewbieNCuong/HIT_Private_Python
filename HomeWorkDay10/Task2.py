import numpy as np

a = np.array([int(i) for i in input("Enter a array: ").split()])
b = np.array([int(i) for i in input("Enter a array: ").split()])
# 1.
print(f"max({a}): {np.max(a)}")
print(f"min({a}): {np.min(a)}")
print(f"mean({a}): {np.mean(a)}")
print(f"std({a}): {np.std(a)}")
print(f"median({a}): {np.median(a)}")
# 2.
c = np.array([a, b])
c = c.T
print(c)
# 3.
d = np.random.normal(np.mean(b), np.std(b), size=(len(b), len(b)))
print(d)
# 4.
print(f"Sum({d}, {d.T}) = {d + d.T}")
print(f"Div({d}, {d.T}) = {d - d.T}")
print(f"Mul({d}, {d.T}) = {d * d.T}")
print(f"Mul({d}, {d.T}) = {np.linalg.pinv(d) * d.T}")
# 5.
e = np.expand_dims(c, axis = 0)
print(e)
print(e.ndim)