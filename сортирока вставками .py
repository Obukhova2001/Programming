from random import randint
N = 20
ok = [randint(0, 100) for i in range(N)]
print(ok)
for i in range(1, N):
    buf = ok[i] # запоминаем ссылку на индекс для последующей подстановки
    j = i - 1
    while ((j>= 0) and (buf < ok[j])):
        ok[j+1] = ok[j]
        j = j - 1
    ok[j+1] = buf
print(ok)