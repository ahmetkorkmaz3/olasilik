adet = int(input("Adet giriniz: "))
dizi = []
toplamlar = 0

for i in range(adet):
  dizi.append(int(input(str(i+1) + ". sayi: ")))

for x in range(adet):
  sayi = dizi[x]
  toplamlar += sayi

aritmatik_ort = toplamlar / adet

ust = 0
for i in dizi:
  ust += (aritmatik_ort-i) ** 2

varyans = (ust/(adet-1))
print("Varyans = {}".format(varyans))

standart_sapma = (ust/(adet-1)) ** (1/2)
print("Standart Sapma = {}".format(standart_sapma))

ust = 0
for i in dizi:
  ust += abs(i-aritmatik_ort)

oms = ust / adet
print("Ortalama Mutlak Sapma = {}".format(oms))

dizi.sort()

q1 = (int)((25 / 100) * len(dizi))
q1 = (dizi[q1-1] + dizi[q1]) / 2

print("Q1 => {}".format(q1))

q3 = (int)((75 / 100) * len(dizi))
q3 = (dizi[q3-1] + dizi[q3]) / 2

print("Q3 => {}".format(q3))

degisim_katsayisi = standart_sapma * 100 / aritmatik_ort

print("Değişim katsayısı => % {}".format(degisim_katsayisi))