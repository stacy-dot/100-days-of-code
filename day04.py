def calculator():
    a=int(input("Enter a no: "))
    b=int(input("Enter a no: "))
    operator=input("Enter an operator:(+,-,/*)")

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero."
    else:
        return "Invalid operator."

result=calculator()
print(result)