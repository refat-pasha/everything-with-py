


b = int(300)
a = int(input())
for i in range(1,a+1):

    bat1,bat2,ballr = input().split()

    ball= b - int(ballr)
    crr = int((int(bat2)/int(ball)*6.00))
    rrr = ((int(bat1)-int(bat2)+1)/int(ballr))*6.00
    print("{:.2f}".format(crr),"{:.2f}".format(rrr))

