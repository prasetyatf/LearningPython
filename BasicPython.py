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
    
