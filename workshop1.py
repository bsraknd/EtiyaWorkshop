# Salary Hike 

# salary tam sayı veri tipinde maaşınızı temsil eden değerdir. hike tam sayı veri tipinde maaşınıza yapılacak olan yüzdelik % bazında zam miktarıdır. (bu değerleri kullanıcıdan alınız.)
# Zammın uygulanması sonucu yeni maaşı ekrana yazdırınız.

newSalary = 0
salary = int(input("Maaşınızı giriniz:"))
raiseRate = int(input("Zam oranını giriniz:"))
newSalary = salary + (salary * (raiseRate/100))
print(newSalary)


# Is Prime?

# `num`  bir pozitif tam sayıdır (integer). `num` sayısı eğer bir asal sayı ise `true` döndürün, değilse `false` döndürün.  (num değerini kullanıcıdan alınız)
# 1 ve kendisinden başka pozitif böleni olmayan 1 den büyük doğal sayılara **asal sayı** denir. 2, 3, 5, 7, 11, 13, 17, 19, 23… sayıları birer asal sayıdır.

asal = 0
num = int(input("Sayı giriniz:"))
if num >= 2:
    for k in range(2,num):
        if num%k == 0:
            asal = asal + 1
        break
    if asal == 0:
        print("Sayı asaldır!")
    else:
        print("Sayı asal değildir!")
else:
    print("Asal sayı 0 ve 1 olamaz!")



