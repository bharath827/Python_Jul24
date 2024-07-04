# operators => symbols to perform some operation on variables or values.


# Arithmetic operators

x = 5 + 3;
print(x)


a = 3;
b = 4;
sum = a + b;
print(sum)



y = 5 - 2;
print(y)

c = 4;
d=4;
subtraction = c -d;
print(subtraction)


z = 4*6
print(z)


w = 15 / 4
print(w)


# Floor division => divides and round downs to the nearest whole number


expr = 15 // 4
print(expr)

print(-17//5)


# Modulus

r = 15 % 4

print(r)


s =  2 ** 3
print(s)

print(2 ** 6)



# Comparision operator => boolean => True or False

a = 15;
b = 13;
print(a == b)


# !=
print(a !=  b)

print(5 > 3)
print(b > a)


print(a<b)
print(a<a)

print(15 < 15)

# >=
result = a>=b
print(result)


print(15>=15)


# <=

print(15<=20)



# Logical Operators

# and  or not

# true * false => flase
# false * false => false
# false * true => false
# true * true => true


a = 5;
b = 10

result = (a==5 and b==10 and 5==5)
print("and operator",result)

# OR operator

# true + false => true
# false +  false => false
# false + true => true
# true + true => true

result = (a==5 or b>10)
print("OR operator",result)



# not
resut = not(a==5)
print(resut)


# Assignment Operators

a = 5;
a = a + 5;

a+= 5

print(a)


a-=5
print(a)


a*= 3; #a =a * 3
print(a)


a//=3;
print(a)

a/=3;
print(a)




b = 10;

b%= 3;
print(b)

a = 3;
a **=2 ;
print(a)


# bit operators
# &&
# ||
#
# 4 => 1 0 0
# 2 => 0 1 0
# -------------
#      0 0 1 => 1


