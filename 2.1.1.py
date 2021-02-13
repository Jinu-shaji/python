#factorial
num=int(input("Enter a number"))
fact=1;
if num<0:
    print("Negative number!!No factorial..")
elif num==0:
    print("Factorial = 1 ")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial(",num,") = ",fact)