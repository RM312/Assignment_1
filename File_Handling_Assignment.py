"""
-> r+ means read and write.
     ->For these mode the file must exist otherwise error is raised.
     ->Both reading and writing operations can take place.

-> w+ means write and read
     ->File is created if does not exist>
     ->If file exists, file is truncated.
     ->Both reading and writing operations can take place.

-> a+ means write and read
     ->File is created if does not exist.
     ->If file exists,file's existing data is retained;new data is appended.
     ->Both reading and writing operations can take place.
"""

#Example of r+
with open('myfile.txt', 'r+') as f:
    f.write("new line \n") 
    
#Exmaple of w+
with open('file.txt', 'w+') as f:  
    f.write("test 1\n")
    f.write("test 2\n")
    f.write("test 3\n")
    f.seek(0)
    print(f.read())
    
#Example of a+
f=open("file.txt","a+")
f.write("test 4")
f.seek(0)
print(f.read())
