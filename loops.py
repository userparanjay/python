# count=0
# while count<5:
#     print("hello",count)
#     count+=1

# num=int(input("Enter number:"))
# x=1
# while x<=10:
#     print(x*num)
#     x+=1
arr=[]
n=1
while n<=10:
    arr.append(n*n)
    n+=1

print(arr)


i=0
list2=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x=int(input("Enter number to search:"))
while i<len(list2):
    if(list2[i]==x):
      print(i)
      break
    i+=1

for el in list2:
   print(el)
else:
   print("end")

# range(start,stop,step)->step is 1 by default
for val in range(10):
   print(val)

for val in range(2,10):#start,stop
   print(val)

for val in range(2,10,2):#start,stop,skip
   print(val)

for val in range(100,0,-1):#start,stop,skip
   print(val)

      