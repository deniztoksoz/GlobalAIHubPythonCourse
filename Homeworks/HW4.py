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
print(ogrbilgi)

#notlar dizisi-listesi(öğrenci adları ve dönemm sonu notları)
print(notlar)

#notlar dizisinin en büyük not en başta en küçük en sonda olarak sıralanmış hali
print(sorted(notlar,key=itemgetter(1),reverse=True))

