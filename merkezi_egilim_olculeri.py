
adet = int(input("Adet giriniz: "))
dizi = []
toplam = 0

for i in range(adet):
  sayi = int(input(str(i+1) + ". sayi: "))
  dizi.append(sayi)
  toplam += sayi

# dizi sıralama 

for i in range(len(dizi)-1):
  for j in range(len(dizi)-1):
    if(dizi[j] > dizi[j+1]):
      temp = dizi[j]
      dizi[j] = dizi[j+1]
      dizi[j+1] = temp

print("Aritmatik ortalama: ", toplam/adet)

# medyan işlemi 
if len(dizi)%2 == 1:
  orta = (len(dizi) + 1) / 2
  print("Medyan eleman: ", dizi[int(orta)])
else:
  orta = int(len(dizi) / 2) - 1
  sonuc = (dizi[orta] + dizi[orta+1]) / 2
  print("Medyan eleman: ", sonuc)

# mod işlemi 

dizi2 = []

maks = -1

for i in range(adet):

  if i-1 == adet:
    sonraki = dizi[i+1]
  else:
    sonraki = None

  if(dizi[i] != sonraki):
    if(maks == dizi.count(dizi[i])):
      dizi2.append(dizi[i])
    elif(maks < dizi.count(dizi[i])):
      dizi2 = []
      dizi2.append(dizi[i])
      maks = dizi.count(dizi[i])

dizi2 = list(set(dizi2))
print("Mod sonucu")
print(dizi2)