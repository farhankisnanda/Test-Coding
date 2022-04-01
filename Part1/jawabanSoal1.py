"""
Dikerjakan dengan menggunakan Python
Program mendeteksi angka
Algoritma:
1. Minta inputan user berupa angka dengan nilai maksimal yaitu 10000
2. Cek apakah angka berupa ganjil atau genap
3. Tampilkan hasil berupa true apabila genap dan false apabila ganjil
Inputan: 
1. Angka
"""

try:
  angka = int(input("Masukkan angka dengan nilai maksimal 10000! \n>> "))
  hasil = True

  if angka <= 10000:
    if angka % 2 == 0:
      hasil = True
    elif angka % 2 != 0:
      hasil = False
    print("")
    print("HASIL PROGRAM")
    print(hasil)
  else:
    print("")
    print("Angka mau melebihi 10000!")

  
except ValueError:
  print("")
  print("Yang kamu masukkan bukan angka bilangan bulat!")
except:
  print("")
  print("Kamu memasukkan inputan yang salah")
