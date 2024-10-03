"""
2. Find the largest element from a given list
without using the library function.

"""


def find_largest(liist):
    largest = liist[0]

    for num in liist[1:]:
        if num > largest:
            largest = num
    return largest


liist = [181, 178, 187, 182, 192, 189, 202, 201]
print(find_largest(liist))
