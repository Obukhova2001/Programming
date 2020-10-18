from random import randint
N=20
ok=[randint(0,100)for i in range(N)]  # заполняем массив случайными числами
print (ok)
for i in range(N-1): # внешний цикл, количество перестановок
    for j in range(N-1-i): # внутренний цикл, сами перестановки
        if ok[j] > ok[j+1]: # сравнение элементов массива
            buf = ok[j]
            ok[j]=ok[j+1]
            ok[j+1]=buf
print(ok)



