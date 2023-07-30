def factor(n):
    
    fac = 1
    while n > 1:
        fac *= n
        n -= 1
    return fac


sp1 = []
sp2 = []

print("Программа по расчету факториалов")

print("Введите любое число:")
 
i = int(input())
    
factor(i)

a = factor(i)

print("Факториал вашего числа:", a)
print("Все факториалы от вашего факториала до 0:")
  
while a > 0:
    sp1.append(a)
    a -= 1

for b in sp1:
    factor(b)
    c = factor(b)
    sp2.append(c)
print(sp2)
