#Set is an unordered collection of datatypes, it doesn't contain a duplicate data
aset={"A","B",1,0,"Data"}
print("The set:",aset)

#Adding an element in set
aset.add(3)
print("After adding an element the set:",aset)

#Removing an element in set
aset.remove(3)
print("After removing an element the set:",aset)

aset1={12,23,34,45,56}
aset2={90,89,67,"Hello",12}
#Union of sets
aset3=aset1.union(aset2) #Or aset3=aset1|(aset2) both are same
print("After Union the set:",aset3)

#Intersection of Sets
aset4=aset1.intersection(aset2) #Or aset4=aset1&(aset2)
print("After Intersection the set:",aset4)

#Difference of Sets
aset5=aset2.difference(aset1)
print("After differencing the set:",aset5)

#Clear() Function is used to clear a specific set
aset5.clear()
print(aset5)
