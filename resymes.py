n, m, s = [int(i) for i in input().split()]
st1 = [] # первая стопка
st2 = [] # вторая
#далее считываем их
for i in range(max(n, m)):
    a, b = input().split()
    if a != '-':
        st1.append(int(a))
    if b != '-':
        st2.append(int(b))    

result = 0 #итоговое количество резюме
summ = 0 #накопленная сумма зарплат
count = 0 #счетчик числа резюме

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


print(result)
