a=5
b=8
if a>b:
    print(a)
else:
    print(b)

x=0
y=135
if x-y==135 or y-x==135:
    print('yes')
else:
    print('no')


def month(num_month: int):
    if num_month in range (3,6):
        print('весна')
    elif num_month in range (6,9):
        print('лето')
    elif num_month in range (9,12):
        print('осень')
    elif num_month in range (1,3) or num_month==12:
        print('зима')
    else:
        print('Введите корректный номер месяца (от 1 до 12)')
month(18)

def y(n1, n2, n3):
    if n1>10 and n2>10 and n3>10:
        print('yes')
    else:
        print('no')
y(12,15,44)


def f(nums: list):
    t=0
    for num in nums:
        if num>0:
            t=t+1
        else:
            t=t
    print(t)
f([-1,-2,-3,-4,-5])

def days(years: int, month: int):
    days_in_years=years*29*12
    days_in_month=month*29
    print(days_in_month+days_in_years)
days(20,5)