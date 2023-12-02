
permanent_password = 1234
num = 3
for attempts in range(3, 0, -1):
    password = int(input('Введите пароль: '))
    if password == permanent_password:
        print('Верный пароль, поздравляю!')
        print('Вы зашли в систему.')
        break
    else:
        num -= 1
        print(f'Неверный пароль, у вас оталось {num} попыток')
if password != permanent_password:
    print('Не удалось войти в систему')