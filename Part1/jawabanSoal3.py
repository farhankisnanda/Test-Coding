"""
Dijawab dengan menggunakan Python
Program mencetak 5 angka berurutan
Algoritma:
1. Minta inputan user berupa angka
2. Lakukan pengulangan angka sebanyak 5 kali dimulai dari angka inputa diakhir 4 angka setelahnya
3. Tampilkan 5 angka tersebut
Inputan:
1. Angka
"""
try:
  angka = int(input("Masukkan angka dengan nilai maksimum 10000! \n>> "))

  print("")
  print("HASIL PROGRAM")
  if angka < 10000:
    for i in range(5):
      print(angka+i)
  else:
    print("Angka kamu melebihi 10000")

except ValueError:
  print("Yang kamu masukkan bukan angka bilangan bulat!")
except:
  print("Kamu memasukkan inputan yang salah!")
