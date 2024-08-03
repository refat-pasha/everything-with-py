


def russianDoll(doll):
    if doll == 1:
        print("all dolls are opened")
    else:
        russianDoll(doll-1)
        print("doll no" , doll)

russianDoll(5)