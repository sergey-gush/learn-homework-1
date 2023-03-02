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
    
    prenatal = -1
    home = 0
    kindergarten = 4
    school = 7
    university = 17
    work = 22
    retiree = 65
    near_death = 124
    person_occupation = {
        prenatal: 'пренатальное развитие',
        home: 'домашнее воспитание', 
        kindergarten: 'детский сад',
        school: 'школа',
        university: 'вуз',
        work: 'работа',
        retiree: 'пенсия'
    }
    
    person_age = int(person_age)
    
    if person_age < prenatal:
        return 'В это время вы ещё на были зачаты'
    elif person_age < home:
        return person_occupation[prenatal]
    elif person_age < kindergarten:
        return person_occupation[home]
    elif person_age < school:
        return person_occupation[kindergarten]
    elif person_age < university:
        return person_occupation[school]
    elif person_age < work:
        return person_occupation[university]
    elif person_age < retiree:
        return person_occupation[work]
    elif person_age < near_death:
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

