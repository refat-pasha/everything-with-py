"""
1. You are given a list of students with their marks in a subject. Write a Python function to store the data in a
dictionary where the key is the student's name and the value is their mark. Then, find and return the student
with the highest mark.
Sample Input: student_scores = [('Alice', 85), ('Bob', 90), ('Charlie', 80)]
Sample Output: {'Alice': 85, 'Bob': 90, 'Charlie': 80}
                            Top Student: Bob with 90 marks

"""


def student_marks(student_scores):
    student_dict = dict(student_scores)
    top_student = max(student_dict, key=student_dict.get)
    top_mark = student_dict[top_student]
    return student_dict, f"Top Student: {top_student} with {top_mark} marks"


student_scores = [('Alice', 85), ('Bob', 90), ('Charlie', 80)]

student_dict, top_student_info = student_marks(student_scores)
print(student_dict)
print(top_student_info)











