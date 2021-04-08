#versiyon 1 - Sadece tek basamak kontrolü yapan kodlama
sayi=int(input("Tek basamaklı bir sayı giriniz : "))
while (0>sayi or sayi>10) :
    print("Girdiğiniz sayı tek basamaklı olmadır.")
    sayi=int(input("Tek basamaklı bir sayı giriniz : "))
#if kontrolü yapmadan çift sayılar direkt yazdırılabilir..
for i in range(0,sayi+1,2):
    print(i,end=" ")
#eğer mod ifadesinin kullanımı görülmek isteniyorsa bu satırlar çalıştırılabilir..
"""    
for i in range(0,sayi+1):
    if (i%2==0):
        print(i,end=" ")
"""
    
#----------------------------------------------------------------------------------------------------------------    
#versiyon 2 - girilen sayı tamsayı mı kontrolü yapan kodlama
while True :
    try:
        sayi=int(input("Tek basamaklı bir sayı giriniz : "))
    except ValueError:
        print("Lütfen sadece tamsayı girin!")
        continue
    if(0<sayi and sayi<10):
        break
    else:
        print("Girdiğiniz sayı tek basamaklı olmadır.")
        
#if kontrolü yapmadan çift sayılar direkt yazdırılabilir..
for i in range(0,sayi+1,2):
    print(i,end=" ")
#eğer mod ifadesinin kullanımı görülmek isteniyorsa bu satırlar çalıştırılabilir..
"""    
for i in range(0,sayi+1):
    if (i%2==0):
        print(i,end=" ")
"""
print("program bitti")
