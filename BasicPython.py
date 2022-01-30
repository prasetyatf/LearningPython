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
