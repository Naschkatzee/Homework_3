d = list (map(int, input ("Введите несколько значений 2-х катетов через пробел: "). split ()))
if len(d) % 2 == 0:
    item_a = 0
    item_b = 1
    number = 1
    while item_a < len (d):
        e = int ((d[item_a]**2 + d[item_b]**2) ** 0.5)
        s = int (d[item_a]*d[item_b]/2)
        print (f'Треугольник {number} с катетами {d[item_a]} и {d[item_b]} имеет площадь {s} и гипотенузу {e} \n')
        item_a += 2
        item_b += 2
        number += 1 
else:
    print ('Вы ввели нечетное количество катетов.')