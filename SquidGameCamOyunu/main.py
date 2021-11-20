import random
x = []
def basamakkontrol(gelensayi,i):
    if x[i]==gelensayi:
        if i == 15:
            print("tebrikler oyunu kazandınız.")
        else:
            print("Tebrikler ",i+1,". aşamadan geçtiniz")
    else:
        print("Üzgünüz ",i+1,". aşamada öldünüz")
        exit()
for i in range(16):
    sayi = random.randint(0, 1)
    x.append(sayi)
print(x)
print("------------------------------")
print("SQUID GAME Oyununa Hoşgeldiniz")
print("Sağ->1 Sol->0")
print("------------------------------")
for i in range(16):
    a=int(input("1 veya 0 seçerek hangi yöne atlayacağınızı seçiniz :"))
    gelensayi=basamakkontrol(a,i)