#----hilangkan "#" pada import utk mengetahui perbedaannya

#from belajarpackage import pembagian #dari folder BelajarPackage akses pembagian.py
#import belajarpackage
#from belajarpackage import *  #--> dari belajarpackage, impor semua file di dalamnya
#import belajarpackage as bp  #--> memanggil belajarpackage dg hanya mengetikkan bp

pembagian = belajarpackage.pembagian 
print(pembagian.bagi(1,2)) #krn import belajarpackage, mk hrs di address scr spesifik

x = pembagian.bagi(1, 2)
print(x)

c = pembagian.bagi(1, 2) #krn di dalam _init_ mengimpor funngsi bagi, maka suggestion disini akan muncul bagi
print(c)
