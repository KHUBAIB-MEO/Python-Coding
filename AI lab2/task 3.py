set1 = {23, "orange", 78.9, True, (5, 6), 50, "apple", 3.14, False, 99}
set2 = {99, "apple", 45.6, 12, "orange", True, 23, 77, (7, 8), 89}

set1.add("KHUBAIB")
print("Add function ", set1)

copySet = set1.copy()
print("Copy function ", copySet)

print("Difference function ", set1.difference(set2))

set1.difference_update(set2)
print("Difference Update function ", set1)

set1.discard(50)
print("Discard function ", set1)

set2.add("KHUBAIB")
print("Intersection function ", set1.intersection(set2))

set1.intersection_update(set2)
print("Intersection Update function ", set1)

print("Disjoint function ", set1.isdisjoint(set2))

print("Sub Set function ", set1.issubset(set2))

print("Super set function ", set1.issuperset(set2))

set2.remove(77)
print("Remove function ", set2)

removeElement = set2.pop()
print("Pop function ", removeElement)
