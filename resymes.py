n, m, s = [int(i) for i in input().split()]
st1 = [] # первая стопка
st2 = [] # вторая
# далее считываем их, причем делаем наибольшую стопку первой
if n >= m:
    for i in range(max(n, m)):
        a, b = input().split()
        if a != '-':
            st1.append(int(a))
        if b != '-':
            st2.append(int(b))
else:
    for i in range(max(n, m)):
        a, b = input().split()
        if a != '-':
            st2.append(int(a))
        if b != '-':
            st1.append(int(b))

result = 0 # итоговое количество резюме
summ = 0 # накопленная сумма зарплат
count = 0 # счетчик числа резюме
num_of_st1 = -1 # номер последнего взятого резюме из 1 стопки

# находим максимальное кол-во резюме в стопке 1,
# при сумме не больше s
for i in range(len(st1)):
    summ += st1[i]
    if summ > s:
        summ -= st1[i]
        if count > result:
            result = count
        break
    count += 1
    num_of_st1 += 1

# начинаем добавлять по 1 резюме из второй стопки, проверяя
# не болше ли сумма, чем s
# если больше, то убираем одно последнее из 1ой стопки и идем 
# дальше по 2ой стопке

for i in range(len(st2)):
    summ += st2[i]
    if summ > s:
        if count > result:
            result = count
        if num_of_st1 >= 0:
            summ -= st1[num_of_st1]
            num_of_st1 -= 1
            count -= 1
        else:
            break
    count += 1

if count > result:
    result = count 

print(result)

'''
def max_resume_in_st(st, s):
    # находит максимальное число резюме в стопке st,
    # при сумме не больше s
    summ = 0
    count = 0
    for i in range(len(st)):
        summ += st[i]
        if summ > s:
            break
        count += 1
    return count

result = max(max_resume_in_st(st1, s), max_resume_in_st(st2, s))
# пробегаемся по обеим стопкам по-отдельности, выбираем максимум
'''
'''
count = 0
summ = 0
for i in range(len(st2)):
    summ += st2[i]
    if summ > s:
        break
    count += 1

if count > result:
    result = count    

count = 0
summ = 0

# далее пробегаемся по возможным комбинациям двух стопок;
# берем 1ый элемент из 1ой стопки, к нему прибавляем все воможные из второй;
# таким образом проходим вглубь 1 стопки, 
# на каждом элементе уходя максимально вглубь 2ой

for i in range(len(st1)):
    summ = sum(st1[:i+1])
    if summ > s:
        break
    count = i+1
    for j in range(len(st2)):
        summ += st2[j]
        if summ > s:
            break
        count += 1
    if count > result:
        result = count 
'''
'''
for i in range(len(st1)):
    summ += st1[i]
    if summ > s:
        break
    count = i+1
    '''
