# sets => unordered collection of unique elements. sets are mutable

# {}  set()

fruits = {"apple", "banana", "cherry", "apple"}



fruits.add("orange")
print(fruits)

fruits.update(["mango", "apple", "grape"])

print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("banana")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)


set1 = {1,2,3,4}
set2 = set1.copy()
print(set2)

subset = {3,4,5,9}
set2 = {6,7,8}


print(subset.isdisjoint(set2))











#
# fruits.remove("banana")
# print(fruits)


#
# numbers = set([1,2,3,4,5,5,6,7])
# print(numbers)
# empty_set = set()








A = {1,2,3,4,5,6,7,8}
B = {1,2,3,4,5,6,7,8}


print(A.issubset(B))
print(B.issuperset(A))

















