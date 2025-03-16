list1 = ["Khubaib", "Meo", 1, 2, 3, 2.74, 3.14, "K"]

list1.append("LAB2")
print("Append function ", list1)

copyList = list1.copy()
print("Copy function", copyList)

print("Count function", list1.count("Khubaib"))

extendedList = ["Apple", "Banana", 21]
list1.extend(extendedList)
print("Extend function ", list1)

print("Index Function ", list1.index(3))

list1.insert(4, "python")
print("Insert function ", list1)

print("Pop function ", list1.pop(6))

list1.remove("Meo")
print("Remove function ", list1)

list1.reverse()
print("Reverse function ", list1)

sortingList = [5, 9, 10, 1, 8, 3, 2, 7, 6, 4]
sortingList.sort()
print("Sort function ", sortingList)

list1.clear()
print("Clear function ", list1)
