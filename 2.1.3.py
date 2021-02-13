li=[]
sum=0
n=int(input("Enter the size of list : "))
print("Enter list items : \n")
for i in range(0,n):
    item=int(input())
    li.append(item)
    sum=sum+item
print("Give list = ",li)
print("Sum of list items = ",sum)