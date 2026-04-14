def myfun(x,y=3):
    return x+y

# print(myfun(2))

def fact(n):
    x=1
    for val in range(1,n+1):
        x=val*x
    return x


print(fact(5))

