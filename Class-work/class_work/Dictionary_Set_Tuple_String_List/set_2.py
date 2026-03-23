set1={1,2,4,4,5,6,7,8}
set2={1,2,44,56,6,778,867}
print(set1.union(set2))

set3=set1.intersection(set2)
print(set3)

set4=set1.difference(set2)
print(set4)

set5=set2.difference(set1)
print(set5)

set1.add(65)
print(set1)
