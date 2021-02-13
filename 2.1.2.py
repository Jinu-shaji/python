#fibanocci series
n = int(input("Number of terms."))

# first two terms
f1 = 1
f2 = 1
count = 0

if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(f1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(f1)
       f3 = f1 + f2
       # update values
       f1 = f2
       f2 = f3
       count += 1