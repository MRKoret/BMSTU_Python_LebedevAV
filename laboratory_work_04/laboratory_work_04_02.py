from random import uniform

n = int(input("Введите кол-во элементов в массиве (от 5 до 30): "))

pol=[]
N=0
if n<5:
    n=5
elif n>30:
    n=30
spisok = [uniform(-5,5) for i in range(1,n+1)]
while N<n:
    if spisok[N] > 0:
        pol.append(spisok[N])
    N+=1

spisok_first=spisok.copy()
spisok.sort(key=lambda x: abs(x), reverse=True)
result=1
for num in spisok[1:-1]:
    result*=num

spisok_second = spisok.copy()
spisok.sort(reverse=True)
print("Изначальный список = ", spisok_first)
print("Сумма положительных элементов = {:1.2f}".format(sum(pol)))
print("Список отсортированный по модулю = ", spisok_second)
print("Произведение элементов, расположенных между min и max по модулю числами = {:1.2f}".format(result))
print("Cписок отсортированый по убыванию = ", spisok)