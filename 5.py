a = list(map(int, input().split()))
c = 0 #счетчик кол-ва пар 
for i in range(len(a)): # элемент списка
    for q in range (i+1, len(a)) : # следующий элемент списка
        if a[i] == a [q]:
            c+= 1
print (c)