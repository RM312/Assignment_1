def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def mod(x,y):
    return x%y
print("Select the Operation\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
while True:
    ch=input("Enter choice:")
    if ch in ('1','2','3','4','5'):
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if ch=='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif ch=='2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif ch=='3':
            print(num1,"*",num2,"=",mul(num1,num2))
        elif ch=='4':
            print(num1,"/",num2,"=",div(num1, num2))
        elif ch=='5':
            print(num1,"%",num2,"=",mod(num1, num2))
        calc=input("Want to do more calculation? (yes/no): ")
        if calc == "no":
          break
    else:
        print("Invalid Input!")
