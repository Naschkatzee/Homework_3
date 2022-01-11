while True:
    try:
        a = list(map(int, input('Значения одного катета n треугольников: ').split()))
        b = list(map(int, input('Значение второго катета n треугольников: ').split()))
        if len(a) == len(b):
            index = 0
            num = 1
            while index < len(a) and len(b):
                c = int((a[index]**2 + b[index]**2) ** 0.5)
                S = int(a[index]*b[index]/2)
                print(f'Треугольник {num} с катетами {a[index]} и {b[index]} имеет площадь {S} и гипотенузу {c}\n')
                index += 1
                num += 1
        else:
            print('InconsistentDataError')
        break
    except ValueError:
        print('NonNumericError')