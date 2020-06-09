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