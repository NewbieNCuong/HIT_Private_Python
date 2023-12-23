import pandas as pd

# 1.
df = pd.read_csv("D:/HIT Private/Python/Pythoncode/Day 10/HomeWorkDay10/Car_sales.csv")
print(df)
# 2.
print(df.shape)
print()
# 3.
df['Sales_in_thousands'].fillna(0.0)
df['__year_resale_value'].fillna(df['__year_resale_value'].mean(), inplace=True)
df['Price_in_thousands'].fillna(df['Price_in_thousands'].median(), inplace=True)
# Thiếu là true, kh thiếu là false
print(f"Dữ liệu thiếu ở mỗi cột:\n {df.isnull().sum()}")
print()
print(df.head())
# 4.
tmp = ["Manufacturer", "Model", "Vehicle_type"]
tmp1 = ["Sales_in_thousands", "__year_resale_value", "Price_in_thousands", "Engine_size", "Horsepower", "Wheelbase", "Width", "Length", "Curb_weight", "Fuel_capacity", "Fuel_efficiency", "Power_perf_factor"]
tmp2 = ["Latest_Launch"]
resviolate = []
for column in df:
    if(column in tmp):
        cnt = 0
        for i in column:
            if(isinstance(i, str)):
                continue
            else:
                cnt += 1
                df.at[i, 'column'] = None
        resviolate.append({column: cnt})
    elif(column in tmp1):
        cnt = 0
        for i in column:
            if(i.isnumeric()):
                continue
            else:
                cnt += 1
                df.at[i, 'column'] = None
        resviolate.append({column: cnt})
    else:
        cnt = 0
        for i in column:
            if(pd.to_datetime(i, errors = "coerce") != None):
                continue
            else:
                cnt += 1
                df.at[i, 'column'] = None
        resviolate.append({column: cnt})

print(resviolate)

# 5.
duplicates = df.duplicated()
print(f"Số dòng trùng lặp: {duplicates.sum()}")
df = df.drop_duplicates()
print(df.head())

# 6.
df["ID"] = df["Manufacturer"] + "_" + df["Model"]
print(df["ID"])
# 7.
Sale = df[['ID', "Sales_in_thousands", "__year_resale_value", "Price_in_thousands"]]
# axis = 1 => để biểu hiện xóa cột
Car = df.drop(["Sales_in_thousands", "__year_resale_value", "Price_in_thousands"], axis = 1)
# 8.
Sale.to_csv("sale.csv")
Car.to_csv("car.csv")