# num1=float(input("enter the number"))
# num2=float(input("enter the number"))

# sum=num1+num2

# print("sum is : ", sum)

# square root using exponentiation

# num=float(input("enter the number:"))
# print("ans is :",num**(1/2))

# # square root using math module
# import math
# num=int(input("enter the number:"))
# print("ans is:",math.sqrt(num))


# area of triangle
# base=float(input("enter the base:"))
# height=float(input("enter the height:"))

# print("enter the area:",0.5*base*height)

# swap two number
# x=float(input("enter the x:"))
# y=float(input("enter the y:"))

# temp=x
# x=y
# y=temp
# print("swapped values are:","x :",x,"y :",y)

# # another method 
# x=12
# y=13
# x,y=y,x



# pos,neg,equal

# num=float(input("enter the number:"))
# if num>0:
#     print("it is positive")
# elif num==0:
#     print("equal")
# else:
#     print("negative")

# num = float(input("enter the number"))
# if num%2==0:
#     print("It is an even number")
# else:
#     print("It is an odd")

# leap year
# year=int(input("enter the year: "))
# if(year % 400 == 0) and (year % 100 ==0):
#     print("leap year")
# elif(year % 4==0) and (year % 100 != 0):
#     print("leap year")
# else:
#     print("not leap year")

# find the largest among three numbers
# x=float(input("enter the x value: "))
# y=float(input("enter the y value: "))
# z=float(input("enter the z value: "))

# if(x>y) and (x>z):
#     print("x is greater")
# elif(y>x) and (y>z):
#     print("y is greater")
# else:
#     print("z is greater")

# prime number
num=float(input("enter the number: "))
if num==1:
    print("not an prime number")
if num > 1 :
    for i in range (2,num):
        if num%i==0:
            print("it is not a prime")
            break
    else:
        print("it is an prime number")