#matba makinesi olacak,
#mürekkebi ve şarjı olacak,
# her 20 calışmada bir dergi ortaya çıkacak
#henüz yeni dergi çıkmadığında yüzde kaçının tamamlandığını gösterecek,
# yeni dergi çıktığındda ona isim verilecebilecek
import time
class makine():
    def __init__(self):
        self.devir=0;
        self.murekkep=100;
        self.sarj=100
        self.dergiler=[]
    def calıs(self):
        if(self.murekkep<=0):
            print("Mürekkep yetersiz")
            time.sleep(2)
        elif(self.sarj<=0):
            print("Şarj yetersiz")
            time.sleep(2)
        else:
           self.devir+=1
           self.murekkep-=3
           self.sarj-=6
           print("makine çalışıyor lütfen bekleyin")
           time.sleep(0.5)
        if self.devir==20:
            self.devir=0
            self.yeniDergi()
    def yeniDergi(self):
        print("Yeni dergi çıktı, hayırlı olsun")
        a=input("dergi ismi giriniz")
        self.dergiler.append(a)
        time.sleep(2)
    def sarjDoldur(self):
        if(self.sarj<100):
            self.sarj+=10
            print("Mevcut şarj-> ",self.sarj)
            time.sleep(2)
    def murekkepDoldur(self):
        if(self.murekkep<100):
            self.murekkep+= 10
            print("mürekkep dolduruldu, mevcut mürekkep->",self.murekkep)

    def mevcutDurum(self):
        print("Makinenin mevcut durumu:")
        print("Kalan mürekkep",self.murekkep)
        print("Kalan şarj",self.sarj)
        print("Toplam çıkarılan dergi sayısı", len(self.dergiler))
        if(len(self.dergiler)>0):
            print("Çıkarılan dergiler:")
            for i in self.dergiler:
                print(i)
        print("Yeni çıkacak olan derginin %",self.devir*5,"kısmı tamamlandı")
        time.sleep(4)

makine1=makine()
print("Matbaya hoş geldiniz")
while True:

    print("-"*15)
    print("Makineyi çalıştırmak için -> 1\n "
          "Mevcut durumu öğrenmek için -> 2 \n "
          "Şarjı doldurmak için -> 3 \n"
          " Mürekkebi doldurmak için -> 4")
    komut=input()
    if(komut=="1"):
        makine1.calıs()
    elif(komut=="2"):
        makine1.mevcutDurum()
    elif(komut=="3"):
        makine1.sarjDoldur()
    elif(komut=="4"):
        makine1.murekkepDoldur()
