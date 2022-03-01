import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

print(csv_data)
print(csv_data.head())
print(csv_data.columns())
print(csv_data['Age'])#akses data melalui kolom
print(csv_data.iloc[5])#akses data melalui baris, 5 adl index
print(csv_data['Age'].iloc[1]) #akses kolom Age, baris ke-2
print("Cuplikan Dataset:")
print(csv_data.head())
