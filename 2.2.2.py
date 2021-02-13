def longest(list2):
    max=len(list2[0])
    temp=list2[0]
    for i in list2:
        if(len(i)>max):
            max=len(i)
            temp=i
    print("longest length word is ",temp,"length",max)
li=[]
n=int(input("Enter size of list"))
print("Enter list elements")
for i in range(0,n):
    item=input()
    li.append(item)
longest(li)