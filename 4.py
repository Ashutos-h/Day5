#Answer 4
list=['Ashu',1,1.25,'Tarun',4.56,23,'Samyak']
print("Original List:")
list_1=[]
list_2=[]
list_3=[]
print(list)
for i in list:
	if type(i)==int:
		list_1.append(i)
	elif type(i)==float:
		list_2.append(i)
	else:
		list_3.append(i)
print("Integer List:")
print(list_1)
print("Float List:")
print(list_2)
print("String List:")
print(list_3)
