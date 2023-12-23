import pandas as pd

df = pd.read_csv("D:/HIT Private/Python/Pythoncode/Day 10/HomeWorkDay10/sale.csv")
df1 = pd.read_csv("D:/HIT Private/Python/Pythoncode/Day 10/HomeWorkDay10/car.csv")

# 1.
sumnumberssellcar = df["Sales_in_thousands"].sum()
print(f"Numbers of sell car: {sumnumberssellcar}")
# 2.
pricemeanofcar = df["Price_in_thousands"].mean()
print(f"Price of mean of car: {pricemeanofcar}")
# 3.
top10maxprice = df.nlargest(10, "__year_resale_value")
print(top10maxprice.head(10))
# 4.
quantity = df1.groupby("Vehicle_type")["Vehicle_type"].count()
print(f"Quantity of Vehicle: {quantity}")
# 5.
print()
mode = df1["Manufacturer"].mode()
print(f"Mode of car: \n{mode}")
# 6.
sort6 = df.sort_values(by = ["Sales_in_thousands", "__year_resale_value", "Price_in_thousands"], ascending=False)
print(f"After sorted:\n {sort6}")
# 7.
merge1 = pd.merge(df, df1, on="ID")
print(f"After merge:\n {merge1.head()}")