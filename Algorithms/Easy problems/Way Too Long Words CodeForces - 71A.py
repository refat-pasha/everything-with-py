a = int(input())


for i in range(a):
    word = input()
    if len(word)>10:
        print(word[0] + str(len(word[1:len(word)-1])) + word[len(word)-1])
    else:
        print(word)