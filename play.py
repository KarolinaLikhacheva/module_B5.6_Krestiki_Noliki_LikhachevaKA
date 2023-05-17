def show_field(f):
    print ('  0 1 2')
    for i in range(len(field)):
        print (str(i)+' '+' '.join(field[i]))


def user_input(f,user):
    while True:
        place=input(f"Ходит {user} .Введите координаты:").split()
        if len(place) != 2:
            print ('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x,y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print ('Вышли из диапазона')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x,y


def win (f, user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indexes = set([i for i,x in enumerate (f_list) if x == user])
    for p in positions:
        if len(indexes.intersection(set(p))) == 3:
            return True
    return False

def start (field):
    count = 0
    while True:
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            show_field(field)
            x,y = user_input(field,user)
            field[x][y] = user

        elif count == 9:
            show_field(field)
            print('Конец игры - НИЧЬЯ!')
            break
        if win (field, user):
            show_field(field)
            print (f"Конец игры. ПОБЕДИЛ - {user}!!!")
            break
        count += 1

field = [['-']*3 for _ in range(3)]

start(field)