#List is an ordered collection of datatypes and it is mutable
alist=[15576,6789.9872,"Data",True]

#Adding a single element
alist.append(67)
print("After adding a single element:",alist)

#Adding multiple elements with the help of list
a=[68,69,70]
alist.extend(a)
print(alist)

#It helps to find the index number of an element
print("The index number:",alist.index(70))

#Adding an element in a specific position
alist.insert(0,"TBH")
print("The elements after inserting in the list:",alist)

#Deleting an element with the help of index number
del alist[0]
print("The values after deleting:",alist)

#Deleting an element with the element's name
alist.remove(70)
print("The values after deleting:",alist)

#It deletes the entire list
del alist
print("The list is deleted")
