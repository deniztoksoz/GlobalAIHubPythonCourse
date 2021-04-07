sayi=int(input("Tek basamaklı bir sayı giriniz : "))
while (0>sayi or sayi>10) :
    print("Girdiğiniz sayı tek basamaklı olmadır.")
    sayi=int(input("Tek basamaklı bir sayı giriniz : "))
for i in range(0,sayi,2):
    print(i,end=" ")
#eğer mod ifadesinin kullanımı görülmek isteniyorsa bu satırlar çalıştırılabilir..
"""    
for i in range(0,sayi+1):
    if (i%2==0):
        print(i,end=" ")
"""
    
    
#girilen sayı tamsayı mı kontrolü yapan versiyon 2
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

for i in range(0,sayi,2):
    print(i,end=" ")
#eğer mod ifadesinin kullanımı görülmek isteniyorsa bu satırlar çalıştırılabilir..
"""    
for i in range(0,sayi+1):
    if (i%2==0):
        print(i,end=" ")
"""
