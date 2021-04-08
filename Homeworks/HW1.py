#birinci yöntem sabit bir dizi üzeirnde bölme ve yazdırma işlemi
dizi=list(range(10))
print("dizinin orjinal hali")
print (dizi)
dizi1=dizi[:5]
dizi2=dizi[5:]
print("\nbölümüş diziler")
print(dizi2,dizi1)

#------------------------------------------------------------------------------------------------------------------------------
#ikinci yöntem kullanıc tarafından uzunluğu belirlenen bir dizinin ortadan ölme ve yazdırma işlemi
kac=int(input("Dizi kaç elemanlı olsun : "))
dizi=list(range(kac))
print("dizinin orjinal hali")
print (dizi)
orta=int(len(dizi)/2)
dizi1=dizi[:orta]
dizi2=dizi[orta:]
print("\nbölümüş diziler")
print(dizi2,dizi1)
