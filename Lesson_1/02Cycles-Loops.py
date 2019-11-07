# coding=utf-8
if 8 / 4.0 == 2:
    print ('OK 1')

elif 8 / 3 == 3:
    print ('OK 2')

else:
    print ('Not OK')

password = ''
if not password:
    true_password = '123456'
else:
    true_password = password

true_password = password if password else '123456'
print(true_password)

password = '546378'
if not password:
    true_password = '123456'
else:
    true_password = password

true_password = password if password else '123456'
print(true_password)

password = None
if not password:
    true_password = '123456'
else:
    true_password = password

true_password = password if password else '123456'
print(true_password)

# Посчитать квадраты 100 чмсел
for i in [1,2,3,4,5,6]:
    print (i**2),
print('')

for i in range(10):
    print (i**2),
print('')

for i in range(1,11):
    print (i**2),
print('')

# List Comprehension (lc)
lc = [i**2 for i in range(1,11)]
print (lc),
print('')

lc = [i**2 for i in range(1,11)][:-2]
print (lc),
print('')

# Посчитаем квадраты только четных чисел
for i in range(1,11):
    if i % 2 == 0: #выделение четных чисел
        print (i**2),
print('')

lc = [i**2 for i in range(1,11) if i % 2 == 0]
print (lc),
print('')

print ('квадраты Нечетных чисел до 100')
lc = [i**2 for i in range(1,101) if i % 2 > 0] #Посчитаем квадраты Нечетных чисел
print (lc),
print('')

print ('квадраты Четных чисел до 100')
lc = [i**2 for i in range(1,101) if i % 2 == 0] #Посчитаем квадраты Четных чисел
print (lc),
print('')

print ('использование while для печати 3-хзначных чисел кратных 13 и подсчета количества таких чисел')
i=1
j=0
while len(str(i)) <= 3:
    if i % 13 == 0:
        print (i),
        j +=1
    i += 1
print('')
print("Nunbers Count: "),
print(j)

