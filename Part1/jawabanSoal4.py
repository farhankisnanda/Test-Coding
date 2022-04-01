"""
Dijawab dengan menggunkan Python
Program pendekteksian urutan angka
Algoritma:
1. Minta inputan array dengan item semuanya angka pada user 
2. Pecah inputan dengan delimiter spasi
3. Ubah nilai item pada array dari str ke angka
4. Cek apakah ada angka pada array tersebut ada yang duplikat atau tidak
5. Cek apakah array tersebut berurutan secara ascending atau tidak
6. Tampilkan hasilnya, true apabila terurut dan false apabila tidak terurut
"""

try:
  array_angka = input("Masukkan angka dengan maksimal sebanyak 50 buah angka dengan pemisah spasi! \n>> ")
  array_angka = array_angka.split(" ")
  
  ubah_ke_angka = []
  for x in array_angka:
    ubah_ke_angka.append(int(x))
    
  array_hasil = list(set(ubah_ke_angka))
  array_hasil.sort()
  
  if len(array_angka) <= 50:
    if ubah_ke_angka == array_hasil:
      hasil = True
    else:
      hasil = False
    print("")
    print("HASIL PROGRAM")
    print(hasil)
  else:
    print("")
    print("Kamu memasukkan angka melebihi 50 buah!")

except ValueError:
  print("")
  print("Yang kamu masukkan ada yang bukan angka!")

except:
  print("")
  print("Kamu memasukkan inputan yang salah!")
