# Open the loop
operand = "Initialize"
while operand != "Q":
    # Accept user input
    num1 = float(input("Please input the first number: "))
    num2 = float(input("Please input the second number: "))
    operand = input("Please input the operator ([A]dd, [S]ubtract, [M]ultiply, [D]ivide, [E]xponent, [R]oot, [Q]uit): ")
    # Uppercase the operand to prevent errors
    operand = operand.upper()
    # Quitting the loop
    if operand == "Q":
        quit()
    # Divide function
    if operand == "D":
        output = num1/num2
        print(num1, '/', num2, '=', output)
    # Multiply function
    if operand == "M":
        output = num1*num2
        print(num1, '*', num2, '=', output)
    # Add function
    if operand == "A":
        output = num1+num2
        print(num1, '+', num2, '=', output)
    # Subtract function
    if operand == "S":
        output = num1-num2
        print(num1, '-', num2, '=', output)
    # Exponent function
    if operand == "E":
        output = num1**num2
        print(num1, '^', num2, '=', output)
    if operand == "R":
        output = num1**(1/num2)
        print(num1, '^/', num2, '=', output)
