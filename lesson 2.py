num = input()

s = {}
for i in range(10):
    s.setdefault(i, num.count(str(i)))
print(s)


@@ -0,0 +1,4 @@
pr = input().split()
for i in range(len(pr)):
  if "@" in pr[i]:
    print(pr[i])

    otv = {}
    while True:
        n = []
        name = input('Введите автора: ')
        if name == 'off':
            break
        else:
            n.append(name)
            n.append(input('Введите позицию в чарте: '))
            n.append(input('Название трека: '))
            dop = {tuple(n[0:2]): n[-1]}
            otv |= dop
    print(otv)



    slov = {'name': 'Maria', 'job': 'student', 'age': '19'}
    l = list(slov.items())
    del l[1]
    slov = dict(l)
    slov['name'], slov['uvl'] = slov['uvl'], slov['name']
    slov.setdefault('new_key', 'new_value')
    print(slov)



    emails = {'gmail.com': ['roma.alimov', 'lera.mini', ],
              'mail.ru': ['olia.popa', 'lol.u', 'sara.olk']}
    for i in emails:
        for j in range(len(emails[i])):
            print(emails[i][j] + '@' + i)