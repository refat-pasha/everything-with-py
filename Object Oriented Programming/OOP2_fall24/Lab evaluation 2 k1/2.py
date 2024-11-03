class Participant:

    def perform_action(self):
        print("this is participant class")


class Student(Participant):
    def __init__(self,view_course_material, submit_assignment):
        self.view_course_material = view_course_material
        self.submit_assignment = submit_assignment
    def perform_action(self):
        print(f"Student course: {self.view_course_material} and submit assignment: {self.submit_assignment}")



class Instructor(Participant):
    def __init__(self, upload_material, grade_assignment, Conduct_class):
        self.upload_material = upload_material
        self.grade_assignment = grade_assignment
        self.Conduct_class = Conduct_class

    def perform_action(self):
        print(f"Instructor Material Upoloaded: {self.upload_material} , grade assignment: {self.grade_assignment} and conduct Class: {self.Conduct_class}")



class teachingAssustabt(Participant):

    def __init__(self, assist_class, grade_assignment):
        self.assist_class = assist_class
        self.grade_assignment = grade_assignment

    def perform_action(self):
        print(f"Teacher assist class : {self.assist_class} and grade assignment: {self.grade_assignment}")



class Course(Student,Instructor,teachingAssustabt):
    def __init__(self,view_course_material, submit_assignment, upload_material, grade_assignment, Conduct_class, assist_class):
        self.view_course_material = view_course_material
        self.submit_assignment = submit_assignment
        self.upload_material = upload_material
        self.grade_assignment = grade_assignment
        self.Conduct_class = Conduct_class
        self.assist_class = assist_class
        
    def perform_action(self):
        print(f"Student course: {self.view_course_material} and submit assignment: {self.submit_assignment}")
        print(f"Instructor Material Upoloaded: {self.upload_material} , grade assignment: {self.grade_assignment} and conduct Class: {self.Conduct_class}")
        print(f"Teacher assist class : {self.assist_class} and grade assignment: {self.grade_assignment}")



#with class class
x = Course(8,10,11,9.9,16,3)

x.perform_action()


#without Course class
# evaluates = {
#     Student(97,16),
#     Instructor(9,7.8,5),
#     teachingAssustabt(8,8.9)
# }
# for evaluate in evaluates:
#     evaluate.perform_action()