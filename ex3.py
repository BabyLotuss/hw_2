my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for item in my_list:
    name = item.split()[-1].title()
    print("Привет,", name)
