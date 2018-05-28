#Answer 1
list=[]
for i in range(10):
	num=int(input("Enter "+str(i+1)+" item:"))
	list.append(num)
for i in list:
	print(str(i)+" ",end='')
	
