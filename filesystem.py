f=open('demo.txt','r')
data=f.read()
print(data)
f.close()


f=open('demo1.txt','w')
data=f.write('addd')
print(data)
f.close()