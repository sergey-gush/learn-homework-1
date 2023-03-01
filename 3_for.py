from collections import Counter

"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
"""
phones =  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

"""
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def phones_sold(sales):
    sum = 0
    for num in range(len(sales)):
        sum += sales[num]
    return sum

def avg_sold(sales):
    sum = phones_sold(sales)
    avg = round(sum / len(sales))
    return avg

def total_sales(sales):
    total = len(sales)
    return total        

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_sum = 0
    total_avg = 0
    total_amount = 0
    print('Всего продано:\n')

    for item in range(len(phones)):
        sum = phones_sold(phones[item]['items_sold'])
        total_sum += sum
        print(f"{phones[item]['product']}: {sum}")

    print('\nСреднее количество продаж:\n')

    for item in range(len(phones)):
        avg = avg_sold(phones[item]['items_sold'])
        print(f"{phones[item]['product']}: {avg}")

    print(f'\nВсего товаров продано: {total_sum}')

    for item in range(len(phones)):
        total = total_sales(phones[item]['items_sold'])
        total_amount += total

    avg_total_sales = round(total_sum / total_amount)

    print(f'\nСреднее количество продаж всех товаров: {avg_total_sales}')
    
if __name__ == "__main__":
    main()

