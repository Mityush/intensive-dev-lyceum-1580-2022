'''Придумал вариант вводить не через дефолтные аргументы, а массивом, чтобы не менять порядок переменных
start, end, step. Можете подсказать, возможно ли написать и с правильным порядком переменных, и без массива?'''
''' Также я ради интереса сделал и дополнительное, и основное задание в одной функции, так принимается или всё же надо двумя?'''

def range(end, start = 0, step = 1, isRight = False):
    a = []
    if step == 0:
        i = 0
        while i < abs(end - start):
            a.append(start)
            i += 1
    elif not isRight and end > 0:
        i = start
        while i < end:
            a.append(i)
            i += step
    elif not isRight and end < 0:
        i = start
        while i > end:
            a.append(i)
            i-=step
    elif isRight and end < 0:
        i = end + step
        while i <= start:
            a.append(i)
            i += step
    else:
        i = end
        while i > start:
            a.append(i)
            i -= step
    return a

def main():
    '''первый аргумент - end, второй - start, третий - step, четвёртый - IsRight'''
    print(range(0))

if __name__ == "__main__":
    main()
