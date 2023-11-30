a = [50, 75, 80, 60, 70, 90, 100, 65, 85, 105]
y = [600, 860, 930, 700, 800, 1040, 1150, 750, 970, 1200]
# w, b = [float(i) for i in input().split()]
c = []
for i in range(len(a)):
    tmp = w * a[i] + b
    c.append(tmp)

sum = 0
for i in range(len(a)):
    sum += (c[i]- y[i]) ** 2
Loss = 1/(2 * len(a)) * sum

# Em đã thử suy ra được muốn loss nhỏ nhất thì với w = 11.5 và b = 3
# Với diện tích 40 m2 thì giá tiền dự đoán là:
w1 = 11.5
b1 = 3
res = w1 * 40 + b1
print("Với diện tích 40 m2 thì giá tiền dự đoán là: {}".format(res))