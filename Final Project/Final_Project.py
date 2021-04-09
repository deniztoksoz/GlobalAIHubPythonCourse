import random as rd
def soruekle():
  while True:
    soru=input("Soruyu yazınız : ")
    cevap=input("Cevabı yazınız : ")
    if input("Bu <%s> sorusuna ait <%s> cevabı ekleyelim mi? (e/h)" %(soru,cevap)).lower()=="e":
      sorular.append((soru,cevap))
    if input("Devam etmek istermisiniz? (e/h)").lower()!="e":
      break

def devammi():
  c=input("Tekrar yarışmak istermisiniz? (e/h) : ")
  if c.lower()=="e":
    return True
  else:
    print("Başka bir yarışmada görüşmek üzere...")
    return False

ssayi=10   #sorulacak sayısı belirleme...
devam=True  #yarışmacı çıkış yapana kadar devam et..
puan=0
sorular=[("Motorsuz uçağa ne ad verilir?","planör"),
 ("İzmit hangi tatlısıyla meşhurdur?","Pişmaniye"),
 ("Osmanlı medeni kanununna ne ad verilir?","Mecelle"),
 ("İki uca da eşit uzaklıkta olan yere nedir?","orta"),
 ("Orman yangını telefon ihbar hattı numarası nedir?","177"),
 ("Seyatnamenin yazarı kimdir?","Evliya Çelebi"),
 ("Balık tutma aracı, bir ip ya da misinaya bağlanan, ucuna metal bir çengel iğne takarak ırmak, deniz veya göllerde balık tutmaya yarayan aracın adı nedir?","olta"),
 ("Bir olayı anlık olarak kayıt altına sesli ve görüntülü olarak kaydeden cihazlara ne ad verilir?","kamera"),
 ("Mahalle ve sokaklarda güvenliği sağlamak için polisle birlikte görev yapan kişilerin mesleği nedir?","bekçi"),
 ("Şanlıurfa şehir merkezinde yer alır. Hz. İbrahim Peygamberin ateşe atıldığı yer olarak bilinen Gölün halk arasındaki adı nedir?","Balıklı Göl"),
 ("Hava sıcaklığını ölçen, ısının birim derecesine adını veren cihazın adı nedir?","termometre"),
 ("Kağıt ve demir paraları basan matbaaların adı nedir?","Darphane"),
 ("Bir saniye kaç salisedir?","60"),
 ("Çocukların en güzel sokak oyunlarının başında gelir. Bir kişinin gözlerinin bağlanarak diğer oyuncuları yakalamaya çalıştığı oyunun adı nedir?","körebe")]


#yarışmacıyla tanışalım
ad=input("Yarışmamıza hoş geldiniz. İsminiz nedir? : ")
print("Merhaba %s, sana toplamda %i soru soracağım. Bu sorulardan en az %i tanesine doğru cevap verirsen yarışmayı kazanmış olacaksın." %(ad.upper(),ssayi,ssayi/2))
print("Eğer istersen yarışmayı kazandığında soru bankamıza sende soru ekleyebilirsin..")
print("Soruları cevaplarken özel isimlerin baş harflerini büyük harf yazmaya dikkat et.")
print("Başarılar..")
input("Devam etmek için bir tuşa bas...")


while devam:
  #yarışmacıya sorulacak soruları seçelim..
  ysoru=[]
  soruid=[]
  while (len(soruid)<ssayi):
    id=rd.randint(0,len(sorular)-1)
    if id in soruid:
      continue
    else:
      soruid.append(id)
      ysoru.append(sorular[id])


  dogru=0
  for i in range(ssayi):
    cevap=input("%i. Soru < %s >  :" %(i+1,ysoru[i][0]))
    if cevap==ysoru[i][1]:
      dogru+=1
      puan+=100/ssayi
      
  if dogru>=ssayi/2:
    print("Tebrikler.. Yarışmayı toplam %i puanla kazandınız.." %int(puan))
    s=input("Yarışmaya yeni soru eklemek istermisiniz? (e/h) : ")
    if s.lower()=="e":
      soruekle()
      devam=devammi()      
    else:
      devam=devammi()  

  else:
    print("Üzgünüm başarısız oldunuz.")
    devam=devammi() 
  
