print('Данная программа проверяет, простое число или нет, если число простое, то вывод - Y, если составное, то - N')
chislo = int(input('Введите число: '))
delitel=2
prostoe=True
for i in range (2, int(chislo**0.5)+1):
    if chislo % delitel !=0:
        prostoe=True
    elif chislo % delitel ==0:
        prostoe=False
        break
    delitel += 1
if prostoe==True:
    print(f'Число {chislo} - Y')
elif prostoe==False:
    print(f'Число {chislo} - N')
