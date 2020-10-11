#PROBLEM 1.5

x = int(input("Harga sebelum diskon : "))
z = int(input("Besar diskon (dalam persen) :"))

y = (100-z) / 100 * x
print("Harga setelah diskon adalah "+str(y))