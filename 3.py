#Answer 3
list=[]
list_2=[]
l=int(input("Enter length of list:"))
for i in  range(l):
	num=int(input("Enter "+str(i+1)+" number:"))
	list.append(num)
for i in list:
	list_2.append(i*i)
print(list_2)
