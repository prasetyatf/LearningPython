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
