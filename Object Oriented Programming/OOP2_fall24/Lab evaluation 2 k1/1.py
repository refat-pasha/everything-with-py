class staff:

    def evaluatee_performance(self):
        print("this is staff class")


class teacher(staff):

    def __init__(self,avg_score,num_of_class):
        self.avg_score = avg_score
        self.num_of_class = num_of_class

    def evaluate_performance(self):
        print(f"Teacher evaluate using avg num: {self.avg_score} and num of class taught : {self.num_of_class}")

class administrator(staff):

    def __init__(self, num_of_event_org, office_efficiency_score):
        self.num_of_event_org = num_of_event_org
        self.office_efficiency_score = office_efficiency_score

    def evaluate_performance(self):
        print(f"Administrator number of event organized: {self.num_of_event_org} and Office Efficiency Score : {self.office_efficiency_score}")


class counselor(staff):

    def __init__(self, counseling_session, stu_feedback_score):
        self.counseling_session = counseling_session
        self.stu_feedback_score = stu_feedback_score

    def evaluate_performance(self):
        print(f"Counselor number of counseling session: {self.counseling_session} and Student Feedback Score : {self.stu_feedback_score}")

evaluates = {
    teacher(97,16),
    administrator(9,7.8),
    counselor(8,8.9)
}
for evaluate in evaluates:
    evaluate.evaluate_performance()