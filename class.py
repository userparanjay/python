class Student:
    name="ajay"
    __rollnumber=123
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("this is a constructor")
    @staticmethod
    def calculate_average(marks):
        sum=0
        for val in marks:
            sum+=val
        return sum/len(marks)


    def printMarks(self):
       return self.calculate_average(self.marks)

s1=Student("karan",[90,80])
print(s1.printMarks())
# print(s1.__rollnumber)