import random

F = open('Слова22.TXT')  # открыть
words = list(F) #сдалал списк
quantity = len(words) #посчитал количество элементов в соем случае слов
quantity = quantity - 1 # Количество слов - 1 чтитает с 0 но по количеству элементов
V = 0 #Счетчик
Replay = [ ] # список для повторов
while True: # Пустой цыкл
    a = input() # Просто ентер для продолжения
    values = random.randint(0, quantity) # Случайное число в массиве
    while values in Replay:# ищет совпадения
        values = random.randint(0, quantity) # рандомит по новой
    else: #Если повторение нет
        Replay.append(values) # Добавляем число чтобы видеть повтарения
        V += 1 # Счетчик + 1
        WordsInMassiv = words[values] # страка с ответом еще не обрезанная
        a = str(WordsInMassiv).split('-', 2) # Обрезаю строну по -
        ai = a[0] # отдельно показываю что первую часть обрезки брать потому что после обрезки получается список из 2 элементов
        print(ai) # Вывожу слово
        i = input() # Просто ентер
        print(words[values], V, quantity) #Ответ
        print(sorted(Replay)) # Просто ключи для проверки повторений
    if len(Replay) == len(words):   #сравнивает если словарь полностью заполнен он равен другому
        print('Перезапуск')
        Replay = [ ] # новый пустой словарь


