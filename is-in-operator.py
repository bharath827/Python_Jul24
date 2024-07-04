# is operator => checks the memory


# a is b


# a = 10;
# b =10;
#
# print(a is b)



list = [1,2,3]
list2 = [1,2,3]
print(list is list2)

msg = "hello"
msg1 = "hello"

print(msg is msg1)



print("------------------")
# in operator => present in a sequence

# value in sequence

str = "Hello World"
print("Hello" in str)
print("bye" in str)

numbers = [1,2,3,4]
print(3 in numbers)


person = {"name":"abc",  "age":30}
print("name" in person)
print("address" in person)


a = [1,2,3]
b=[1,2,3]
c=a;

print(a is b) #false
print(a is c) #true


word = "devops"
letters = ['d','e','v','o','p','s']
dict = {
    'd':1,
    "e":2,
    "v":3,
    "o":4,
    'p':5,
    's':6
}

print('---------------------')

print('v' in word) #true
print('x' in word) #false
print('v' in letters)  #true
print('x' in letters) #false
print('v' in dict) #true
print('x' in dict) #false