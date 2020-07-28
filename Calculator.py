first_number = float(input("Type your first number: "))
operator = input("Type your operator: ")
second_number = float(input("Type your second number: "))

def calculate():
    if operator == "+":
        return(first_number + second_number)
    elif operator == "-":
        return(first_number - second_number)
    elif operator == "*":
        return(first_number * second_number)
    elif operator == "/":
        return(first_number / second_number)
    else:
        return("This operator does not exist")

print(calculate())

