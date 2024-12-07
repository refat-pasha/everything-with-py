x = int(input("enter salary: "))

def bonus(x):
    if x > 20000 < 25000:
        total = 0
        house = x/2
        medical = x *.1
        spacial_bonus = 2000
        total += x + house + medical + spacial_bonus
        return total

    elif x > 25000 < 30000:
        total = 0
        house = x / 2
        medical = x * .15
        spacial_bonus = 2000
        total += x + house + medical + spacial_bonus
        return total
    else:
        return "no bonus"

print(bonus(x))
