a, b, c = list(map(int, input().split()))
ch1, ch2 = input().split()
print("{:02d}/{:02d}/{:02d}".format(b, a, c))
print("{:02d}/{:02d}/{:02d}".format(c, b, a))
print("{:02d}-{:02d}-{:02d}".format(a, b, c))

