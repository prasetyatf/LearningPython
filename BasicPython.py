#i've learned basic python at Kelas Terbuka YT channel(https://www.youtube.com/c/KelasTerbuka)
#what i've learned this time is about variable operation
-------------------------------------------------------------
#operasi value yg bertype data beda, tdk bisa. pengecualian pd "*"
a="b"
b="A"
print('2 * "a" = ',2*"a")
#print('2+"a"',2+"a")

#bukti python procedural. dpt mggunakan var yg sama, tp yg dipake var yg paling bawah
a=5
b=2
a=a+b
b=a-b
a=a-b
print('bukti python itu procedural. ini adalah', a)

#tupple
(a,b)=(2,5)
(a,b)=(b,a)
print('ini tupple', a,b)

(c,d)=(1,2)
(e,f)=(3,4)
print((c,d)+(e,f))
#error tupple hny bs concatenate(digabung)print((c,d)-(e,f))

#a adalah string. string bisa digunakan layaknya list
a= 'harsh'
b=a[1:len(a)]
print(a[0])
print(b)

l=[1,2,3,4,5]
print('l=[1,2,3,4,5]')
print('ini list l', l[1:9])#tidak error walopun char yg diminta > jml list
print('ini list l', l[-1])#mengakses urutan list dr kanan

p=[1,2]+[3,4]#menggabungkan list
print('[1,2]+[3,4] = ', p)
-------------------------------------------------------------
#what i've learned this time is about logic operator
-------------------------------------------------------------
#and, or, xor
a=True
b=False
print("NOTE: a=True, b= False")
print("AND===")
print("a and a = ",a and a)
print("a and b = ",a and b)
print("b and b = ",b and b)
print("OR===")
print("a or a = ",a or a)
print("a or b = ",a or b)
print("b or b = ",b or b)
print("XOR=== nulisnya(^)")
print("a xor a = ",a ^ a)
print("a xor b = ",a ^ b)#jika hanya ada 1 yg benar mk benar
print("b xor b = ",b ^ b)
-------------------------------------------------------------
#sorry for this part i've mistaken about how git works ;)
-------------------------------------------------------------
#what i've learned this time is about Comparation operation <,>,<=,>=,==,!=,is,is not
-------------------------------------------------------------
a=2
b=5
cek1 = a > 3
cek2=a>=3
cek3=a==3
cek4=a!=3
cek5=a is 3
cek6=a is not 3
cek7=a==b
cek8=[]
cek9=[]

print("a > 3 =", cek1)#dapat berkerja pd syntax literal
print("a >= 3 =", cek2)#dapat berkerja pd syntax literal
print("a == 3 =", cek3)#dapat berkerja pd syntax literal
print("a != 3 =", cek4)#dapat berkerja pd syntax literal
#contoh perbandingan objek dan literal.  a == 3. a itu objek, 3 itu literal. gunakan == aja ben ra mumet
print("a is 3 =", cek5)
print("a is not 3 =", cek6)
print("a == b =", cek7)
print("cek8 is cek9 = ",cek8 is cek9)#id1 and id2, value1 and value2
print("cek8 == cek9 = ",cek8 == cek9)#id1 or id2, value1 or value2
-------------------------------------------------------------
#what i've learned this time is about List
-------------------------------------------------------------
data=["saya","adalah","tegar"]
datas=data[0]
#mengakses list
print("data ke-0", data[0])
print("data ke-(-2)", data[-2])
print("mengakses data dengan data[a:b] = ", data[0:3])#[a=dimulai dari 0 : b=dimulai dari 0]
#memotong list/slicing
print("data ke-(1-3)", data[0:3])#dimulai dari data ke-0 sampai sebelum data ke-3
print("data ke-(2-3)", data[1:3])#dimulai dari data ke-1 sampai sebelum data ke-3
print("data2 sebelum data ke-1", data[:1])#[:b]dimulai dari tak hingga sampai sebelum data ke-1
print("data2 sebelum data ke-1 dr blkng", data[:-1])#dimulai dari tak hingga sampai sebelum data data ke-(-1)
print("memunculkan data ke-2 saja", data[1], data[1:2])#dimulai dari data ke-1 sampai sebelum data ke-2
print("data2 ssudah data ke-1", data[1:])#dimulai dari data ke-1 sampai tak hingga
#'+' dan '-' menunjukkan arah
#menambah data
data2=["ada","haha"]
data3= data + data2
data4= data2 + data
apen=data4.append(666)
apen2=data4.append(input("masukkan: "))
print(data3)
print(data4)
#mengubah data
data[0]="kamu"
ubahdata=data
print(ubahdata)
#list dalam list
gabdata=data,data2
print(gabdata)
#mengakses list dalam list
aksesmulti=gabdata[1][1]
print(aksesmulti)
-------------------------------------------------------------
#what i've learned this time is about If Else
-------------------------------------------------------------
data=[0,9,8,7,6,5]
cek1=99
cek2=int(input("masukkan angka = "))
if cek1 in data:
    print(cek1,"ada di data")
elif cek2 in data:
    print("data inputan pertama tidak ada. sedangkan", cek2, "ada di data")
else:
    print("semua data inputan tidak ada di dalam list")
-------------------------------------------------------------
#what i've learned this time is about looping(for)
-------------------------------------------------------------
#iterate itu mengecek 1/1 objek lalu mengeksekusinya
data1=[1,2,3,4]
data2=["aku","adalah","tegar"]
data3="tegar"
for i in data1:#i adalah iterate, data1 adalah objek. maka objek hrs didefinisikan sedang iterate tidak
    print(data1) #ngeprin isi data1 sejumlah data1    
for i in data3: #t+e+g+a+r=5
    print(data2)
for i in range(1,6,2):#dimulai dr 1, berakir <6, penambahan 2
    print(i)
#note: masih banyak objek lain selain 'in range'
-------------------------------------------------------------
#what i've learned this time is about looping(while)
-------------------------------------------------------------
#dalam while juga berlaku continue,break,pass
x=0#integer
start=True#boolean
while x<=5:#perulangan
    print(x)#0
    x+=1#x+1
    #dst
while start:
    print(x)
    if x == 6:
        start=False
    x+=1
while start:
    print(x)
    if x == 6:
        start=False
    x+=1
else:
    print("selesai")
-------------------------------------------------------------
#what i've learned this time is about looping(while)
-------------------------------------------------------------
#break = menghentikan loop
#continue = melanjutkan looping ke iterator selanjutnya dan melewati iterator saat ini
#pass = tidak melakukan apaapa
print("continue=======")
for i in range(1,11):
    if i == 4:
        print("ini adalah", 4)
        continue#ketika i=4, alur eksekusi dikembalikan ke baris for atas
    print(i)  

print("break=======")
for x in range(1,11):
    if x == 4:
        print("ini adalah", 4)
        break#ketika i=4, alur eksekusi for berhenti/keluar
    print(x)

print("pass=======")
for m in range(1,11):
    if m == 4:
        print("ini adalah", 4)
        pass#bingung??
    print(m)

print("break=======")
for i in range(7,11):
    if i == 9:
        print("ini adalah", 9,"break---")
        break
    print(i)

print("continue=======")
for i in range(7,10):
    if i == 8:
        print("ini adalah", 8)
        continue
    print(i)
else:
    print("selesai")
