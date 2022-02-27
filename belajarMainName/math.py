def penjumlahan(a, b):
    x = a
    y = b
    return f"{x}+{y} = {x+y}"

def pengurangan():
    c = "ini pengurangan"
    print(c)
    return c

print(__name__) #jika dirun di file ini mk hasilnya __main__
#jika file yg mengimpor file ini akan muncul nama file ini

if __name__ == '__main__':
    pengurangan()
