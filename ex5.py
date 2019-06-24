"""""
Week #1 Exercise 5 - calculator
"""""
def read_until_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def calc(num1,operator,num2):
    res = 0

    if(operatot == "+"):
         res = num1 + num2
    elif(operatot == "-"):
         res = num1 - num2
    elif(operatot == "*"):
         res = num1 * num2
    elif(operatot == "/"):
         res = num1 / num2
    elif(operatot == "^"):
         res = num1 ** num2
    else:
        raise ("Error!!")

    print(f"The result = {res}")

def read_until_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

x = read_until_number("select a number")
operatot = input("eneter an operator (+,-,*,/,^)")
y = read_until_number("select a number")

try:
    calc(x,operatot,y)
except Exception:
    print("Invalid operator!!")



