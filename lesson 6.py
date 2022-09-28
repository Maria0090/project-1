create_dict():
    power_of_number = 2
    dictionary = dict()
    for i in range(1, 11):
        dictionary[i] = pow(i, power_of_number)
    print(dictionary)



numbers = "6,7,8"
Numbers = dict()
for i in range(0,10):
    Numbers[i] = numbers.count(str(i))


