a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print("If you want to add enter + and if you want to subtract -")
mathfunction = input("- + * or / : ")


def addition():
    print(a + b)


def subtraction():
    print(a - b)
    

def multiplication():
    print(a * b)


def division():
    print(a / b)


if mathfunction == "+":
    addition()


if mathfunction == "-":
    subtraction()
    
if mathfunction == "*":
    multiplication()
    
if mathfunction == "/":
    division()