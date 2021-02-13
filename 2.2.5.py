square=lambda x:x*x
rectangle=lambda x,y:x*y
triangle=lambda x,y:0.5*x*y
s=int(input("enter side of square : "))
print("Area of square = ",square(s))
l=int(input("enter length of rectangle : "))
b=int(input("enter breadth of rectangle : "))
print("Area of rectangle = ",rectangle(l,b))
h=int(input("enter height of triangle : "))
ba=int(input("enter base of triangle : "))
print("Area of triangle = ",triangle(h,ba))

