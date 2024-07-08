
import math
'''
square1= [x**2 for x in range(10)]

print(square1)

def square(num):
    return num*num

def cube(num):
    return num*num*num


try:
    num = int(input("enter the num: "))
    pi = 3.14
    print("sqaure of the number is :", square(num))
    print("cube of the nuber is :   ", cube(num))
    print("squaroot of the given number using math module:", math.sqrt(num))
    print("perimeter of the number", 4*num)
    
    print("area of the circle is ", pi*num**2,"sq")

except ValueError:
    print("inetr inetrger without decimal")

def TotalMarks():

    marks1 = int(input("enete marks of sub1: "))
    marks2 = int(input("enter marks of sub2: "))
    marks3 = int(input("enter marks of sub3: "))

    avg = (marks3+marks2+marks1)/3

    print("average of marks is :", int(avg))

TotalMarks()
'''


'''def OddEven():
    num = int(input("enter the num: "))

    if num%2 == 0:
       print("number is even")
    else:
       print("number is odd")
OddEven()

def BiggestNum():
    a = int(input("enter the num: "))
    b = int(input("enter the num: "))
    c = int(input("enter the num: "))

    if a >= b and a >= c:
        print(a, "a is bigger")
    elif b >= a and b >= c:
        print(b, "b is bigger")
    else:
        print(c, "c is bigger")

BiggestNum() '''

def LeapYear():
  while True:
    a = int(input("enter the year: "))
    if a % 4 ==0:
        if a % 100 ==0:
            if a % 400 ==0:
                print("it is a leap year")
            else:
                print("not a leapyear")
        else:
            print("not a leap year")
    else:
        print("not a leap year")

LeapYear()
