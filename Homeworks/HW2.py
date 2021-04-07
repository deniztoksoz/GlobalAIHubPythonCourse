sayi=int(input("Tek basamaklı bir sayı giriniz : "))
while (0>sayi or sayi>10) :
    print("Girdiğiniz sayı tek basamaklı olmadır.")
    sayi=int(input("Tek basamaklı bir sayı giriniz : "))
for i in range(0,sayi,2):
    print(i,end=" ")
