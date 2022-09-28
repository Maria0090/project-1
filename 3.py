food = input()
food = food.lower()
if (food == 'завтрак'):
    print('Каша')
elif (food != 'завтрак'):
    print('Ты хочешь плотно поесть?')
    goodMeal = input()
    goodMeal = goodMeal.lower()
    if (goodMeal == 'да'):
        print('Плов')
    else:
        print('Котлета с пюре')



payment = int(input('Введите сумму к оплате: '))
hour = int(input('Введите текущий час: '))

if 8 <= hour <= 22:
    if 10 <= hour <= 12:
        print(f'сумма к оплате равна - {payment / 2}')
    elif 20 <= hour <= 22:
        print(f'сумма к оплате равна - {payment / 4}')
    else:
        print(f'сумма к оплате равна - {payment}')
else:
    print('Мы закрыты')



productOne = int(input())
productTwo = int(input())
productThree = int(input())
Amount = productOne + productTwo + productThree
if ((productOne < productTwo) and (productOne < productThree) and (productTwo < productThree)):
    print('Акция!', Amount/2)
elif ((productOne > productTwo) and (productOne > productThree) and (productTwo > productThree)):
    print('Акция', Amount/4)
else:
    print('К оплате:',Amount)



category = input()
category = category.lower()
if (category == 'продукты'):
    price = int(input('Введите цену: '))
    if (price > 0) and (price < 100):
        print('Попробуйте нашу выпечку!')
    elif (price >= 100) and (price < 500):
        print('Попробуйте орехи в шоколаде')
    elif (price >= 500):
        print('Попробуйте экзотические фрукты!')
else:
    print('Загляните в товары для дома!')


Number = int(input())
if ((Number%10)%2 == 0) and (sum(map(int,str(Number)))%3 == 0):
    print('Делится')
else:
    print('Не делится')


