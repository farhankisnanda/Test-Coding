"""
Dikerjakan dengan menggunakan Python
Program mendeteksi kata akhiran 'ha'

Algoritma:
1. Minta kalimat dari user
2. Cek apakah kalimat mengandung akhiran 'ha'
3. Tampil true apabila ditemukan, false jika tidak

Inputan:
1. Kalimat
"""

try:
  kalimat = input("Masukkan sebuah karakter/kata/kalimat! \n>> ")
  kalimat = kalimat.lower()
  
  if kalimat[-2:] == "ha":
    hasil = True
  else:
    hasil = False
  
  print("")
  print("HASIL PROGRAM")
  print(hasil)

except:
  print("Kamu memasukkan inputan yang salah!")
