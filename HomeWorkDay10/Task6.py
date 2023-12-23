import numpy as np
import pandas as pd

row = 50

age = np.random.randint(18, 23, row)
major = ["CNTT", "KTPM", "KHMT", "HTTT", "CNDPT"]
major_random = np.random.choice(major, row)

contests = ["Typing", "Lập trình thi đấu", "Web", "AI-Tank", "Rung chuông vàng"]
contest_data = {contest: np.random.choice(np.append(np.arange(0, 11), np.nan), row) for contest in contests}

# 1.
df = pd.DataFrame({
    "Tuổi" : age,
    "Ngành": major_random,
    **contest_data
})

print(df)

# 2.
df["ID"] = np.arange(1, 51)
df["Tổng cuộc thi"] = df.iloc[:, 3:].count(axis = 1)
df["Tổng điểm"] = df.iloc[:, 3:7].sum(axis = 1)
print(df)

# 3.
print()
top3scoremax = df.nlargest(3, "Tổng điểm")[["ID", "Tuổi", "Ngành"]]
print(f"Top 3 max score: {top3scoremax}")

# 4.
print()
cnt = df[df["Ngành"] == "CNTT"]
rescnt = cnt.iloc[:, 3:7].count().idxmax()
print(f"CNTT has many joiner: {rescnt} ")

# 5.
print()
mostjoiner = df.iloc[:, 3:7].count().idxmax()
leastjoiner = df.iloc[:, 3:7].count().idxmin()
print(f"Most joiner: {mostjoiner} ")
print(f"Least joiner: {leastjoiner} ")
