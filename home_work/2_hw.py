def task_1()->str:
    q: int=135
    w: float=7.5431
    e: str='Пушков'
    r: list=[2,3,5,7,11]
    t: bool=True
    print(q, 'относится к типу', type(q))
    print(w, 'относится к типу', type(w))
    print(e, 'относится к типу', type(e))
    print(r, 'относится к типу', type(r))
    print(t, 'относится к типу', type(t),'\n')
task_1()

def task_2()->str:
    a = [1, 2, 3, 5, 8, 13, 21]
    print(a[0:3])
    print('Ответ: данная последовательность - числа Фибоначчи(каждое следующее число равно сумме двух предыдущих)','\n')
task_2()

def task_3(a: int)->int:
    return a ** 2
print('квадрат числа равен', task_3(125))