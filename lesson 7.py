# 1
A = {1, 2, 3, 4, 5, 6}
B = {4, 16, 1, 3, 8, 2}
print(A & B)


# 2
#testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
#printSet = set(testList)
d = set[1,2,2,[3,4],(1,2,3),"1",{1,2,3}]
e = set(range(5))
print(e)

immutable = ["sdv", "asc",  "xkx", "kcla", "as", "dac"]

for i in range(len(e)):
    if type(e[i]) not in immutable:
        print("False")
    break
else:
    print("True")



#3
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
print(len( newspaper | magazine) - both)


#4
first = "0 0 0 0 0 0 0"  # Вывод должен быть 0
second = "1 1 1 0 0 0 0"  # Вывод должен быть 3
third = "1 1 1 1 1 1 1"  # Вывод должен быть 1

A, B, C, D, E, F, G = map(int, first.split())
print(A + B + C - F + D + E - G)

A, B, C, D, E, F, G = map(int, second.split())
print(A + B + C - F + D + E - G)

A, B, C, D, E, F, G = map(int, third.split())
print(A + B + C - (F + D + E - G))
