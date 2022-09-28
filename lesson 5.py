game = input('Введите настольную игру: ')
gameList = []
while (game != '0'):
    if (game not in gameList):
        gameList.append(game)
    else:
        print('Игра уже была записана')
    game = input('Введите настольную игру: ')
gameList.sort()
print(gameList)



evaluations = [2,3,4,5,3,4,5,5,5,5,2,2,4]
count = len(evaluations)
count3 = evaluations.count(3)
count4 = evaluations.count(4)
count5 = evaluations.count(5)
countList = [count3,count4,count5]
progress = sum(countList)/count*100
print(evaluations)
print(countList)
print(progress)



all_fives():
    while True:
        grades = input()
        amount_of_5 = grades.count('5')
        buffer = grades.split(' ')
        amount_of_all = len(buffer)
        print((amount_of_5 * 100) / amount_of_all)



surname = input('Введите фамилию: ')
Post = input('Введите должность: ')
countList = []
count = int(input('Введите количество учеников (0 - закончить ввод): '))
while (count != 0):
    countList.append(count)
    count = int(input('Введите количество учеников (0 - закончить ввод): '))
personalInformation = [surname,Post,countList]
print(personalInformation)



numbers = [2]
increases = True
for i in range(1,len(numbers)):
    if (numbers[i] - numbers[i-1] != 1):
        increases = False
    if (increases == False):
        break
if (len(numbers) == 1):
    increases = False
if (increases == True):
    print('Да')
else:
    print('Нет')