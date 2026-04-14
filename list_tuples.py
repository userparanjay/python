# lists=>mutable
marks=[97.0,80.5,66.4,45.1,"Karan"]
marks[4]="data"
print(marks[1:2])
print(marks)
# print(marks[0])
# print(type(marks))
print(len(marks))
#tuple
tup=(1,2,4,3,3)
tup[3]='asda'#error
print(tup.count(3))