import Work
import fractions

def main():
    # Задача 1
    inpt = int(input('Введите число: -> '))
    print(f"Результат функции task_1 -> 0x{Work.task_1(inpt)}")
    print(f"Результат функции hex -> {hex(inpt)}")
    print('----------------------------------------------------------------------------------------')
    '''
        >>>
        Введите число: -> 67855858
        Результат функции task_1 -> 0x40b65f2
        Результат функции hex -> 0x40b65f2
    '''
    # Задача 2
    a = '3/4'
    b = '2/7'
    print(f"Результат функции task_2 сложение -> {Work.task_2(a, b)}")
    print(f"Результат функции fractions сложение-> {fractions.Fraction(3, 4) + fractions.Fraction(2, 7)}")
    '''
        Результат функции task_2 сложение -> 29/28
        Результат функции fractions сложение-> 29/28
    '''
    print('========================================================================')
    print(f"Результат умножения дробей task2 -> {Work.task_2(a, b, key=2)}")
    print(f"Результат функции fractions умножение-> {fractions.Fraction(3, 4) * fractions.Fraction(2, 7)}")
    '''
        Результат умножения дробей task2 -> 6/28 -> 3/14
        Результат функции fractions умножение-> 3/14
    '''


if __name__ == '__main__':
    main()