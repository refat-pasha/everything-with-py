# run time error
"""t = int(input())
for i in range(t):
    sentence = input().split()
    sentence_len = len(sentence)
    prob = math.factorial(sentence_len)
    if prob > 20:
        prob /= 2
        print(f"1/{math.trunc(prob)}")

    else:
        print(f"1/{math.trunc(prob)}")"""

#this code work fine

import sys
from collections import Counter


# this function is used for returning factorial of a number
def fact(num):
    total = 1
    for j in range(1, num + 1):
        total *= j
    return total


def main():
    n = int(input())
    for _ in range(n):
        # taking input string
        str_input = input()
        # splitting the string into words
        words = str_input.split()
        num = len(words)

        # storing factorial of num to total
        total = fact(num)

        # counting occurrences of each word
        word_count = Counter(words)

        # checking how much words are the same and then updating value of total
        for count in word_count.values():
            total //= fact(count)

        # printing output
        print(f"1/{total}")


if __name__ == "__main__":
    main()







