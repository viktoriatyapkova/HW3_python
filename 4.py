n = int(input()) # кол-во дней
a = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
c = 0 #повторение цикла 
i = 0 #индекс в списке с кашами
while c != n: #пока не вышли за кол-во дней
    if i > len(a) - 1:
        i = 0 #если номер дня больше последнего индекса списка, то он обнуляется
        print(a[i])
    else:
        print(a[i]) #если номер дня меньше последнего  индекса списка, то  выводим очередь каш
    c += 1 
    i += 1