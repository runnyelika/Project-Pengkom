#PROBLEM SET 1.4

x = int(input("Masukkan 3 angka terakhir NIM Anda: "))

m = 1+(x % 2)
f = 7+(x % 3)
k = 9+(x % 4)

print("Anda berada di kelas ")
print("Kelas "+str(m)+" - Matematika")
print("Kelas "+str(f)+" - Fisika")
print("kelas "+str(k)+" - Kimia")

print()
print("Powered by Hughie")