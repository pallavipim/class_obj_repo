# To calculate the area of the rectangle

class AreaRect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calculate_area(self):
        return self.l * self.b

area1 = AreaRect(11,2)
area2 = AreaRect(11,5)
print(area1.calculate_area())
print(area2.calculate_area())


# To greet a person:
class Employee:

    def __init__(self, fname, lname, email):
        self.fname=fname
        self.lname=lname
        self.email=email

    def fnGreet(self):
        print("Hello, Welcome to my home "+ self.fname + " " + self.lname)

obj=Employee("pallavi", "pimple", "pal10@gmail.com")
obj.fnGreet()



# To calculate the simple interest:

class Simple_interest:

    def __init__(self, principal, rate, time_period):
        self.principal=principal
        self.rate=rate
        self.time_period=time_period

    def calculte_interest(self):
        return self.principal* self.rate* self.time_period

Int1=Simple_interest(10000, 10, 10)
print(Int1.calculte_interest())

Int2=Simple_interest(3000, 12, 3)
print(Int2.calculte_interest())