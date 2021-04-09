#yöntem 1
#öğrenci adları kullanıcıdan alınıyor.. Randomize olarak 0 ile 100 arasında 3 adet not atanıyor. 
import random as rnd
ogrbilgi={}
notlar=list()
for i in range(1,6):
    s={}
    s["ad"]=input("%i. öğrencinin adını giriniz : " %i)
    s["vize"]=rnd.randint(0,100)
    s["proje"]=rnd.randint(0,100)
    s["final"]=rnd.randint(0,100)
    ogrbilgi[i]=s

#öğrenciler kütüphanesi
print("Öğrenci Bilgileri Kütüphanesi")
print(ogrbilgi,"\n")

#öğrenci notları hesaplanıp listeye alınıyor..
for k,v in ogrbilgi.items():
  donemnotu=round(((v["vize"]*0.3)+(v["proje"]*0.3)+(v["final"]*0.4)))
  notlar.append((v["ad"],donemnotu))

#notlar listesi(öğrenci adları ve dönem sonu notları)
print("öğrenci adları ve dönemm sonu notları")
print(notlar,"\n")

#notlar listesinin en büyük not en başta en küçük en sonda olarak sıralanmış hali

takas = True
while takas:
  takas = False
  for i in range(len(notlar) - 1):
    if notlar[i][1] < notlar[i + 1][1]:
      notlar[i], notlar[i + 1] = notlar[i + 1], notlar[i]
      takas = True
print("öğrenci adları ve dönem sonu notları sıralı hali")
print(notlar,"\n")


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#yöntem 2 sıralama için operator kütüphanesi kullanılıyor. öğrenci kütüphanesinde dönem sonu notları yazılıyor.
#öğrenci adları kullanıcıdan alınıyor.. Randomize olarak 0 ile 100 arasında 3 adet not atanıyor. Dönem sonu notu hesaplanıyor..
import random as rnd
from operator import itemgetter
ogrbilgi={}
notlar=list()
for i in range(1,6):
    s={}
    s["ad"]=input("%i. öğrencinin adını giriniz : " %i)
    s["vize"]=rnd.randint(0,100)
    s["proje"]=rnd.randint(0,100)
    s["final"]=rnd.randint(0,100)
    s["donemnotu"]=round(((s["vize"]*0.3)+(s["proje"]*0.3)+(s["final"]*0.4)))
    ogrbilgi[i]=s
    notlar.append((s["ad"],s["donemnotu"]))

#öğrenciler kütüphanesi
print("Öğrenci Bilgileri Kütüphanesi")
print(ogrbilgi,"\n")

#notlar dizisi-listesi(öğrenci adları ve dönemm sonu notları)
print("öğrenci adları ve dönemm sonu notları")
print(notlar,"\n")

#notlar dizisinin en büyük not en başta en küçük en sonda olarak sıralanmış hali
print("öğrenci adları ve dönemm sonu notları sıralı hali")
print(sorted(notlar,key=itemgetter(1),reverse=True))
