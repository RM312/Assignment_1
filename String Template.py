#String Template Class
'''In the String module, Template Class allows us to create simplified syntax for output specification. 
The format uses placeholder names formed by $ with valid Python identifiers.'''

from string import Template
Student = [('Anumita',56), ('Neha',45), ('Ushnangshu',89)]
t = Template('Hi $name, you have got $marks marks')
for i in Student:
    print (t.substitute(name = i[0], marks = i[1]))

from string import Template
t = Template('The value of x is $x')
print (t.substitute({'x' : 65568}))
