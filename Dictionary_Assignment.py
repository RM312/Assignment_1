"""Dictionaries is an ordered collection of datatypes and  do not allow to store duplicate values. 
It used to store the data values in Key:Value pairs."""
adic={"A":"Lenovo","B":"Pink","C":2022}
print("The Dictionary:",adic)

#Adding key:value pairs in dictionary
adic["D"]="New"
print("After adding new key:Value Pairs:",adic)

#Update a value pair
adic["A"]="Apple"
print("After updating a key:Value Pairs:",adic)

#Update or adding 2 or multiple value pairs in a key
adic["A"]="Lenovo","Apple"
print("After adding 2 Value Pairs:",adic)

#To print a specific Key:Value Pair in dictionary with the help of key Value
print("To print a specific Key:Value Pair in dictionary with the help of key Value:",adic["A"])

#To delete a specific Key:Value Pair in dictionary
del adic["D"]
print("After deleting a key:value pair:",adic)

#Merging a dictionary
bdic={"E":20999}
adic.update(bdic)
print("After Merging a dictionary:",adic)

#To delete entire dictionary
del adic
print("The dictionary is deleted")
