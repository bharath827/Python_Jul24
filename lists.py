# Lists => Data => ordered collection of data and it can be any data type
# mutable


empty_list = []


               # 0    1       2      3
str = "Hello"
    #  01234
# indexing => way to access individual elements

#
# captured_char = str[3]
# print(str[0])
# print(captured_char)



int_list = [1,2,3,4,5]

mixed_lists = [1, "apple", 3.154, True]
               # -4    -3      -2    -1

# print(int_list[0])
#
# print(mixed_lists[3])
#
# print(int_list[-1])
# print(mixed_lists[-3])

# slicing => way to access a subset of elements from a list.

# list[start:stop:step]



numbers = [0,1,2,3,4,5,6,7,8,9]

sub_list = numbers[2:5]
print(sub_list)

sub_list = numbers[0:5]
print(sub_list)


sub_list = numbers[6:]
print(sub_list)


sub_list = numbers[:4]
print(sub_list)

sub_list = numbers[:]
print(sub_list)


sub_list = numbers[-3:]
print(sub_list)

sub_list = numbers[:-3]
print(sub_list)


# numbers = [0,1,2,3,4,5,6,7,8,9]

sub_list = numbers[1:7:2]
print(sub_list)


sub_list = numbers[::2]
print(sub_list)

sub_list = numbers[::-1]
print(sub_list)






# numbers = [0,1,2,3,4,5,6,7,8,9]


numbers[2] = "hello"
print(numbers)


numbers[-1] = 10

numbers[2:5] = [20,30,40]
print(numbers)

# [0, 1, 20, 30, 40, 5, 6, 7, 8, 10]
numbers[3:5] = []


# [0, 1, 20, 5, 6, 7, 8, 10]
numbers[2:2] = [50,60]  #[0, 1, 50, 60, 20, 5, 6, 7, 8, 10]


numbers[2:3] = [30]
print(numbers)

# numbers = "123"
# print(numbers)

# print(numbers)


# methods

# append => its adds an element to end of the list
print("-----------------------------------------------")
lists = [1,2,3]
lists.append(4)
print(lists)

# extentd => append the elements from another iterable

num1 = [1,2,3]
mixd_val = [4,"hello", "python", True]

num1.extend(mixd_val)
print(num1)


# insert => insert an element at as specified position

num1 = [1,2,4]
num1.insert(2, 3)
print(num1)

# remove() => removes first occurance

numb = [1,2,3,3,4,2,5,6,7]
numb.remove(2)
numb.remove(6)
numb.remove(3)

print(numb)


# pop() => last element

values = ["Java", "Python", "javascript", "C", "C#"]

popped_element = values.pop()
print(values)
print(popped_element)


values.pop(1)
print(values)
# ['Java', 'javascript', 'C']

# clear => removes all the elements from the list

values.clear()
print(values)


# index() => index of first occurance of specified value

numbrs = [1,2,3,2,4,5]
print(numbrs.index(5))


# count()
print(numbrs.count(5))

# sort()

numbers = [4,5,1,2,3]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers) #[5, 4, 3, 2, 1]
#

# reverse
numbers.reverse()
print(numbers) #[1,2,3,4,5]


# copy()
copied_numbers = numbers.copy()
print(copied_numbers, "copied_numbers")
