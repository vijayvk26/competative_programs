class Employee:
    def __init__(self,employee_name,designation,salary,overTimeContribution={}
                 ,overTimeStatus=False):
        self.employee_name=employee_name
        self.designation=designation
        self.salary = salary
        self.overTimeContribution = overTimeContribution
        self.overTimeStatus = overTimeStatus




class Organization:
    def __init__(self,employee_list):
        self.employee_list = employee_list
        self.bonus_list = []

    def check_eligibility(self,overtime_threshold):
        for i in self.employee_list:
            total = sum([j for j in i.overTimeContribution.values()])

            if total > overtime_threshold:
                i.overTimeStatus = True
            print(i.employee_name,i.overTimeStatus)
            if i.overTimeStatus is True:
                self.bonus_list.append(total)

    def calculate_bonus(self,rate_per_hour):
        total = sum(self.bonus_list)
        print(rate_per_hour * total)

no_of_employees=int(input())
employee_list = []

for i in range(no_of_employees):
    name = input()
    designation = input()
    salary = int(input())
    count_of_months = int(input())
    overTimeDict = {}
    for j in range(count_of_months):
        month = input()
        hours = int(input())
        overTimeDict[month] = hours

    empobj = Employee(name,designation,salary,overTimeDict)
    employee_list.append(empobj)

overTimeThresh = int(input())
rate = int(input())


orgobj = Organization(employee_list)

orgobj.check_eligibility(overTimeThresh)
orgobj.calculate_bonus(rate)






