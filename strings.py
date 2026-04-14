
firstname=input("Enter your name:")
number=int(input("Enter a number:"))
marks=int(input("Enter your marks:"))
print("length is",len(firstname))
print("count of a in name :",firstname.count("a"))
#if-elif-else
if(marks>=90):
    if(marks>=95):
        print("you have A+ grade")
    else:
        print("you have A grade")
elif(marks<90 and marks>=80):
    print("you have B grade")
elif(marks<80 and marks>=70):
    print("you have C grade")
else:
    print("you have D grade") 

if(number%7==0):
    print("is a multiple of 7")
else:
    print("is not a multiple of 7")
