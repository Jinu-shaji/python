
def factor(x):
    print("the factors of number",x,"is")
    for i in range(1,x+1):
        if(x%i==0):
            print(i)

n=int(input("Enter a number"))
factor(n)