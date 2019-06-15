num1 = float(input("enter first number"))
ope = input("enter the operator")
num2 = float(input("enter second number"))

if(ope == "+"):
    print(num1 + num2)

elif(ope == "-"):
    print(num1 - num2)

elif(ope == "*"):
    print(num1 * num2)

elif(ope == "/"):
    print(num1 / num2)

else:
    print("invalid operator")
