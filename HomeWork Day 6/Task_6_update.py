import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.array([[50, 75, 80, 60, 70, 90, 100, 65, 85, 105]]).T
y = np.array([[600, 860, 930, 700, 800, 1040, 1150, 750, 970, 1200]]).T

# Đánh giá trước khi làm bài
# plt.plot(X, y, 'or')
# plt.axis([40, 110, 590, 1220])
# plt.show()

# Create Xbar
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.inv(A), b)
print(w)

w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(50, 115, 2)
y0 = w_0 + w_1*x0
# result
print(w_0 + w_1 * 40)


plt.plot(X, y, 'or')
plt.plot(x0, y0)
plt.axis([40, 110, 590, 1220])
plt.show()