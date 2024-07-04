# dictionaries => unordered collections of items.
# key value
# mutable => we can change or modify


person1 = {
    "name" : "Pradeep",
    "age" : "20",
    "city" : "Bengaluru",
    "Job" : "teacher"
}

print(person1)


person2 = dict(name="Rajkumar", age="30", city="Mysore", job="actor")
print(person2)

print(person2["name"])

name = person1["name"]
print(name)



city = person2.get("city")
print(city)


# person1 = {
#     "name" : "Pradeep",
#     "age" : "20",
#     "city" : "Bengaluru",
#     "Job" : "teacher"
# }

person1["email"] = "pradeep@gmail.com"
print(person1)

person1["age"] = 40
print(person1)

del person1["Job"]
print(person1)

email = person1.pop("email")
print(person1)




# person1 = {
#     "name" : "Pradeep",
#     "age" : "20",
#     "city" : "Bengaluru",
#     "Job" : "teacher"
# }


# methods
keys = person1.keys() #return list of keys
print("keys of person1",keys)

values = person1.values()
print("values of person1", values)


items = person1.items() #[('name', 'Pradeep'), (),()]
print("Items of person1", items)


person1.update({"Job":'Software Developer', "phone":"1234567890"})
print(person1)

# person1.clear()
# print(person1)

