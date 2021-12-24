"""
create a class passenger having attributes
name,age,disttravelled

create a function which takes passenger objects list,fare_rate
calculate fare of the ticket with tax
for passengers of age >=60 and <12  = no tax
for other passengers tax = 12%

print passenger_name and ticket_fare
"""


class passenger:
    def __init__(self,name,age,disttravelled):
        self.name =name
        self.age=age
        self.disttravelled = disttravelled



def calculate_fare(passenger_list,fare_rate):
    pass_list = []
    for i in passenger_list:
        fare = i.disttravelled *fare_rate
        if i.age>=60 or i.age<12:
            pass
        else:
            fare = fare + (fare * 0.12)
        pass_list.append((i.name,fare))
    return pass_list

no = int(input())
passenger_list = []
for i in range(no):
    name = input()
    age = int(input())
    distance = int(input())
    passenger_list.append(passenger(name,age,distance))


li = calculate_fare(passenger_list,10)

for i in li:
    print(i[0],i[1])





