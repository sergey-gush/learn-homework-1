"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def occupation(person_age):
    
    kindergarten = range(7)
    school = range(7, 18)
    university = range(18, 24)
    work = range(24, 66)
    retiree = range(66, 123)
    person_occupation = {
        kindergarten: 'детский сад',
        school: 'школа',
        university: 'вуз',
        work: 'работа',
        retiree: 'пенсия'
    }
    
    person_age = abs(person_age)

    if person_age in kindergarten:
        return person_occupation[kindergarten]
    elif person_age in school:
        return person_occupation[school]
    elif person_age in university:
        return person_occupation[university]
    elif person_age in work:
        return person_occupation[work]
    elif person_age in retiree:
        return person_occupation[retiree]
    else:
        return 'Ваш возраст превышает рекорд долгожительства!' 
  

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    age = int(input("Сколько вам лет? "))
    user_occupation = occupation(age)
    print(f'Ваш род занятий: {user_occupation}')
    

if __name__ == "__main__":
    main()

