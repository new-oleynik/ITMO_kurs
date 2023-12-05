num=3
if num>=0:
    print('число положительное либо равное 0')
else:
    print('число отрицательное')

str_1='test'
str_2='test1'
if str_1 in str_2:
    print('yes')
else:
    print('no')

num_float=-5
if num_float>0:
    print('положительное число')
elif num_float==0:
    print('ноль')
else:
    print('отрицательное число')

permit_print=True
if num>0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('печать запрещена')

kurs_bak=[1,2,3,4]
kurs_mag=[5,6]
kurs_asp=[7,8,9]
kurs=10
if kurs in kurs_bak:
    print('Вы являетесь бакалавром')
elif kurs in kurs_mag:
    print('Вы являетесь магистром')
elif kurs in kurs_asp:
    print('Вы являетесь аспирантом')
else:
    print('Введите корректный год обучения')

num=125
if num>100 or num<-100:
    print('-')
else:
    print('+')