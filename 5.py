#Answer 5
list=[]
for i in range(2,101):
        isPrime=True
        for j in range(2,i):
                if i%j==0:
                        isPrime=False
        if isPrime==True:
                list.append(i)
print(list)
