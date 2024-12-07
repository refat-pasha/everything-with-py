x = int(input("enter salary: "))

def bonus(x):
    if x>= 20000 <= 30000:
        bonus = x * .05
        return bonus + x
    elif x> 30000:
        bonus = x * .1
        return bonus + x
    elif x< 20000:
        return " no Bonus"
    else:
        return "not valid salary!"

print(bonus(x))
