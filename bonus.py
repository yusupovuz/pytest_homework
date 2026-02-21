def bonus_time(salary, bonus):
    a = bonus == True and salary*10 or salary
    return "$"+str(a)