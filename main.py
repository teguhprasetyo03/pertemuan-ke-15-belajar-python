import modul as mx
import platform
from modul import say_hello
# lambda expression

# tanpa menggunakan lambda
def square_sum(x,y):
    return x**2 + y**2
print(square_sum(20,20))

# menggunakan lambda
# cara pertama
a  = lambda x,y: x**2 + y**2
print(a(20,20))

# menggunakan lambda
# cara pertama
hasil_penjumlahan = lambda a,b : a+b
print(hasil_penjumlahan(10,20))

# cara kedua
# bisa langsung di isi expresinya
hasil_pengurangan = (lambda x,y : x-y)(34,10)
print(hasil_pengurangan)

# hasil import
mx.say_hello("Andi", "Teguh")

x = mx.orang1["age"]
y = mx.orang1["name"]
Z = mx.orang1["country"]
print("My name is "+y, x, "My country is", Z)

x = mx.orang2["age"]
y = mx.orang2["name"]
Z = mx.orang2["country"]
print("My name is "+y, x, "My country is", Z)

x = platform.system()
print(x)

print(say_hello("joni ", "albert"))