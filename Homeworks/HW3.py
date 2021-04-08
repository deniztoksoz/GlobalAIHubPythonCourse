#Yöntem 1 - kullanıcı adı ve şifre aynı anda kontrol ediliyor..
kontrol=0
while True:
    kadi=input("Kullanıcı Adınızı Giriniz : ")
    pword=input("Şifrenizi Giriniz : ")
    if(kadi=="dt" and pword=="123"):
        print("Sisteme girişiniz sağlandı.")
        break
    elif(kadi=="dt" or pword=="123"):
        print("Kullanıcı adı veya şifrenizi yanlış girdiniz.")
        kontrol+=1
        if(kontrol==3):
            print("3 defa başarısız giriş denemesi yaptınız.\nDaha sonra tekrar deneyiniz.")
            break
        continue
    else:
        print("Sisteme kayıtlı değilsiniz.")
        break
#------------------------------------------------------------------------------------------------------------------
#Yöntem 2 - Önce kullanıcı adı sonra şifre kontrolü yapılıyor..
kontrol=0
kadi=input("Kullanıcı Adınızı Giriniz : ")
if(kadi=="dt"):
    while True:
        pword=input("Şifrenizi Giriniz : ")
        if(pword=="123"):
            print("Sisteme girişiniz sağlandı.")
            break
        else:
            print("Şifrenizi yanlış girdiniz.")
            kontrol+=1
            if(kontrol==3):
                print("3 defa başarısız giriş denemesi yaptınız.\nDaha sonra tekrar deneyiniz.")
                break
            continue
else:
    print("Kullanıcı adınızı bulamadık. Sisteme kayıtlı değilsiniz.")
    print("Önce kayıt oluşturmayı denemelesiniz.")

#------------------------------------------------------------------------------------------------------------------
#Yöntem 3 dict kullanarak kayıt girişi uygulaması. Yeni Kullanıcı Ekleme dahil..
kulls = {"dt":"123","af":"345","bc":"abcedf"}
giris_kontrol=True
while giris_kontrol:
    kontrol=0
    kadi=input("Kullanıcı Adınızı Giriniz : ")
    if(kadi in kulls):
        while True:
            pword=input("Şifrenizi Giriniz : ")
            if(pword==kulls[kadi]):
                print("Sisteme girişiniz sağlandı.")
                giris_kontrol=False
                break
            else:
                print("Şifrenizi yanlış girdiniz.")
                kontrol+=1
                if(kontrol==3):
                    print("3 defa başarısız giriş denemesi yaptınız.\nDaha sonra tekrar deneyiniz.")
                    break
                continue
    else:
        print("Kullanıcı adınızı bulamadık. Sisteme kayıtlı değilsiniz.")
        cevap=input("Kayıt oluşturmak istiyormusunuz? (e/h)")
        if cevap=="e":
            while True:
                kadi=input("Kullanıcı Adınızı Giriniz : ")
                if(kadi in kulls):
                    print("Bu kullanıcı adı kayıtlı. Başka bir ad giriniz.")
                    continue
                pword=input("Şifrenizi Giriniz : ")
                kulls[kadi]=pword
                print("Şimdi giriş yapabilirsiniz..")
                break
        else:
            print("Sistemimizi ziyaret ettiğiniz için teşekkür ederiz.")
            break

