a = int(input('Bir sayı giriniz:'))
b = int(input('İkinci bir sayı giriniz:'))
def OBEB(a, b):
    while b != 0:
        a, b = b, a % b
    return(a)



print("********************")
print("OBEB:", OBEB(a, b))
print("********************")
istek = input("Devam etmek ister misiniz?:(Evet/Hayır)")
while istek == "Evet":
        a = int(input('Bir sayı giriniz:'))
        b = int(input('İkinci bir sayı giriniz:'))
        print("********************")
        print("OBEB:", OBEB(a, b))
        print("********************")
        istek = input("Devam etmek ister misiniz?:(Evet/Hayır)")
        
