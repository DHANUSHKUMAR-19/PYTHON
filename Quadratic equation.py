from math import *
a=float(input("enter a 1 number\n"))
b=float(input("Enter 2nd number\n"))
c=float(input("Enter 3rd number\n"))
d=b*b-4*a*c

if a==0:
    print("Solution can't be find\n")
elif  d>0:
    print("Roots are real and distinct\n")
    x1=(-b+sqrt(d))/2*a
    x2=(-b-sqrt(d))/2*a
    print("Rules are %f, %f\n"%(x1,x2))
elif d<0:
    print("roots are real and imaginary\n")
    x1=(-b+sqrt(fabs(d)))/2*a
    x2=(-b-sqrt(fabs(d)))/2*a
    print("x1+ix2=%f+i%f\n"%(x1,x2))
else:
    x1=x2=(-b+sqrt(d))/2*a
    print("roots are ",x1,x2)
