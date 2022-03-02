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
print(csv_data['Age'].iloc[5:10]) #mengakses kolom & baris sama seperti mengakses list
print(csv_dataset.describe(include=all)) #mengetahui info stats scr cepat
print(csv_data.describe(exclude=['O']) #mengabaikan data non-numerik
print(csv_data.isnull()values.any()) #mengecek apa ada data kosong

#mengisi missing value dg mean/median. ingat di kursus lain, ada hal2 yang lebih detail ttg missing value
print(csv_data.mean())
print("Dataset yang masih terdapat nilai kosong ! :")
print(csv_data.head(10))

csv_data=csv_data.fillna(csv_data.mean()) #mengisi missing value dg mean. .median() utk mengisi dg median
print("Dataset yang sudah diproses Handling Missing Values dengan Mean:")
print(csv_data.head(10))
