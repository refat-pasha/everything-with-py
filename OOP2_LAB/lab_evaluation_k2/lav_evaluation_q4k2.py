"""
4. Given is a nested tuple.
Write a program to modify the list's first item (22)
inside the following tuple to 222.
Sample Input: (11, [22, 33], 44, 55)
Sample Output: (11, [222, 33], 44, 55)
"""

Sample_Input = (11, [22, 33], 44, 55)
Sample_Input[1][0] = 222
print(Sample_Input)
