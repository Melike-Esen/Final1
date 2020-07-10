#SORU1
m= int(input("Gün Giriniz:"))
e = int(input("Ay Giriniz:"))
l = int(input("Yıl Giriniz:"))

esen = {1:"Ocak", 2:"Şubat", 3:"Mart" , 4:"Nisan", 5:"Mayıs", 6:"Haziran", 7:"Temmuz", 8:"Ağustos" , 9:"Eylül",10:"Ekim", 11:"Kasım", 12:"Aralık"}
melike = (esen[l])
print(m,"-",melike,"-",l)
#SORU2
m = int(input("16'dan Küçük ve Negatif Olmayan Sayı Giriniz: "))
e=1

while m>16 or m<0:
    m=int(input("Girdiğiniz sayı hatalıdır,bir daha deneyiniz."))

if  m >= 9 and m < 16:
 def recur_dizi(m):
     if m >= 9 and m < 16:
       return 9 and 16
     return (2*m)+ recur_dizi(m-1)
 l = 0
 for e in range(m + 1):
    i = 2 * e
    l = i + l
    m = m + 1
    print("Girilen sayı 9 ve 16 arasındaıdr,Toplam:", l)
else:
    print("Aralık dışı bir sayı girildi")

if m >= 0 and m < 9:
    def recur_dizi(m):
        if m >= 0 and m < 9:
            return 9 and 0
        return [3 * m] + recur_dizi(m - 1)
    l = 0
    for e in range(m + 1):
        i = 3 * e
        l = i + l
        m = m + 1
    print("Girilen sayı 0 ve 9 arasındadır,Toplam:", l)
else:
    print("Aralık dışı bir sayı girildi")
#SORU3
#Şifrelenecek_kelime=melikeesenli
#Hatalı çalışıyor.Çarpımları matematikte yaptığım şekilde yapmasını sağlayamadım.
melike_esen_li =(13,5,12),(9,11,5),(5,19,5),(14,13,5)
A = [[1,2,-1],
     [2,5,2],
     [-1,-2,2],]
Mel=[[13,
      5,
     12],]
m1=[[0],[0],[0],]
for  l in range(len(A)):
    for i in range(len(Mel[0])):
        for k in range(len(Mel)):
            m1[l][i] +=A[l][k]*Mel[k][i]
print(m1)

Ike=[[9,
      11,
      5],]
m2=[[0],[0],[0],]
for  l in range(len(A)):
    for i in range(len(Ike[0])):
        for k in range(len(Ike)):
            m2[l][i] +=A[l][k]*Ike[k][i]
print(m2)
Ese=[[5,
      19,
      5],]
m3=[[0],[0],[0],
    ]
for  l in range(len(A)):
    for i in range(len(Ese[0])):
        for k in range(len(Ese)):
            m3[l][i] +=A[l][k]*Ese[k][i]
print(m3)
Nli= [[14,
       13,
       5],]
m4=[[0],[0],[0],
    ]
for  l in range(len(A)):
    for i in range(len(Nli[0])):
        for k in range(len(Nli)):
            m4[l][i] +=A[l][k]*Nli[k][i]
print(m4)

#SORU4
m=[]
for e in range(2,12):
    l = 0
    for i in range(2,e):
        if e%i == 0: l=1
    if l == 0:
        m.append(e)
print(m)
