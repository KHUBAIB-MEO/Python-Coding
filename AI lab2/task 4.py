information = {
    "Name": "KHUBAIB",
    "Gender": "Male",
    "CNIC": "42201-2378673-7"
}

dict2 = information.copy()
print("Copy function : ", dict2)

print("Clear function : ", dict2.clear())

print("Fromkeys function : ", dict.fromkeys(information))

print("Get function : ", information.get("Name"))

print("Items function : ", information.items())

print("Keys function : ", information.keys())

value = information.setdefault("Name", 10)
print("Setdefault function Key exist : ", value)

value1 = information.setdefault("Age", 18)
print("Setdefault function Key does not exist : ", information)

information.update(Age=20)
print("Update function : ", information)

print("Values function : ", information.values())

print("Pop function : ", information.pop("Age"))

print("PopItem function : ", information.popitem())
