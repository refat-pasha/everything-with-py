class Employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def display(self):
        print(f"Employee Name :{self.name} \nSalary : {self.employee_id}")
class Developer(Employee):
    def __init__(self,programming_lang,exp_year):
        self.programming_lang = programming_lang
        self.exp_year = exp_year

    def display(self):
        print(f"Developer Name : {self.name} \nID : {self.employee_id} "
              f"Programming Language : {self.programming_lang} \nExprience Year : {self.exp_year}")
class SeniorDeveloper(Developer):
    def __init__(self,name,employee_id,programming_lang,
                 exp_year,project_managed,mentoring_team_size):
        self.name = name
        self.employee_id = employee_id
        self.programming_lang = programming_lang
        self.exp_year = exp_year
        self.project_managed = project_managed
        self.mentoring_team_size = mentoring_team_size
    def display(self):
        print(f"Developer Name : {self.name} \nID : {self.employee_id} "
              f"\nProgramming Language : {self.programming_lang} \nExprience Year : {self.exp_year}"
              f"\nProject Managed : {self.project_managed} \nTeam Size : {self.mentoring_team_size}")

x = SeniorDeveloper("Refat",101,"Python",3,5,10)
x.display()