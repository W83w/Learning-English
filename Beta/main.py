import random
Button = 3

while Button > 0:
    Carts = random.randrange(0, 2, 1)
    print(Carts)
    if Carts == 0:
        print('count')
        print('Посмотреть ответ 1 продолжать 2')
        ButtonContinual = input()
        if ButtonContinual == 1:
            print('"abc"".count("a") --- count - счетчик счтитает совпадения')

    if Carts == 1:
        print('division')
        print('Посмотреть ответ 1 продолжать 2')
        ButtonContinual = input()
        if ButtonContinual == 1:
            print('division - деление')




