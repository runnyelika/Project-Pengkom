#PROBLEM SET 1.3

x = float(input("Masukkan A "))
y = float(input("Masukkan B "))
z = float(input("Masukkan C "))
u = float(input("Masukkan D "))

blowca = 2 ** (-1/2)
total_x = z - (blowca*y) + (blowca*u)
total_y = x - (blowca*y) - (blowca*u)

dist = (total_x ** 2 + total_y ** 2) ** (1/2)
cing = print("Jarak harta karun: "+str(dist))
print("{:.2f}".format(dist))