a=input("Masukkan nama anda:")
b=input("Masukkan mata kuliah:")
c=input("Masukkan grup:")

x=a.split(" ")

nb=x[len(x)-1]
nd=x[0]

ns=x[0:len(x)-1]

nx=" ".join(ns)

print("Hallo! %s, %s"%(nb,nx))
print ("%s tergabung dalam kelas %s pada grup %s"%(nd,b,c))
