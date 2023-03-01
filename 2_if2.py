"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def strings(str1, str2):
    if type(str1) is not str or type(str2) is not str:
        return 0
    elif str1 == str2:
        return 1
    elif len(str1) > len(str2) and str2 != 'learn':
        return 2
    elif str2 == 'learn':
        return 3

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    not_string = strings('string', 5)
    print(f'В функцию переданы не строки: {not_string}')
    equal = strings('string', 'string')
    print(f'Строки идентичны: {equal}')
    first_longer = strings('сестра таланта', 'краткость')
    print(f'Первая строка длиннее: {first_longer}')
    second_is_learn = strings('python', 'learn')
    print(f'Вторая строка "learn": {second_is_learn}')
    second_longer = strings('краткость', 'сестра таланта')
    print(f'Вторая строка длиннее: {second_longer}') 

    
if __name__ == "__main__":
    main()

