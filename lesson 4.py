def music_recommendation():
    for i in range(0, 3):
        print("Введите предпочтение", i + 1)
        user_input = input()
        print("Предпочтение ", user_input, " учтено")
    print("Система рекомендаций настроена!")



while True:
    choice = input('Введите game/off \n')

    if choice == 'off':
        break

    elif choice == 'game':
        print('Игра "угадай число" У тебя 3 попытки, вводи число \n')
        trying = 0
        for _ in range(0, 3):
            answer = int(input())
            if answer == 5:
                print('Победа!')
                break
            else:
                print('Неверно! Еще попытка ')
                continue
        else:
            print('Попытки кончились ')
            continue



def login():
    forbidden = 'fyug'
    while True:
        user_input = input('Enter login')
        for i in user_input:
            if i in forbidden:
                print(i)



while True:
        user_input = input()
        if user_input != 'off':
            print('Спасибо, ваш отзыв принят!')
        else:
            print('Система предпочтений настроена')
            break



while True:
    cost = int(input('Введите сумму покупки: '))
    discount = int(input('Введи скидку в %: '))
    if cost == 0:
        break
    else:
        price = cost - (cost / 100 * discount)
        print(f'Цена за товар:')
        continue