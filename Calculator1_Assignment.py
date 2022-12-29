a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=str(input("Enter the Operator:"))
if c=='+':
    print("The Addition of two numbers:",a+b)
elif c=='-':
    print("The Subtraction of two number:",a-b)
elif c=='*':
    print("The Multiplication of two number:",a*b)
elif c=='/':
    if b!=0:
        print("The Division of two numbers:",a/b)
    else:
        print("The Division is Invalid!")
else:
    print("You have enter wrong operator.")
