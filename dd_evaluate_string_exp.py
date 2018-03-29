one = '1 * -2 + -3 * 4' # -14
two = '1 + 135 / 134' # 2
three = '-234' # -234

# Given a string seperated by spaces, evaluate the expression and return the result


def add_string(str):
    expressions = str.split(" ")
    if len(expressions) == 1:
        return expressions[0]

    addition_opperations = []

    for counter, value in enumerate(expressions):
        if value == "/":
            to_div = int(expressions[counter - 1]) / int(expressions[counter + 1])
            addition_opperations.append(to_div)
        elif value == "*":
            to_mult = int(expressions[counter - 1]) * int(expressions[counter + 1])
            addition_opperations.append(to_mult)
        elif value == "+" or value == "-":
            if expressions[counter - 1]:
                addition_opperations.append(expressions[counter - 1])
            addition_opperations.append(value)

    result = int(addition_opperations[0])

    for counter, value in enumerate(addition_opperations):
        if value == "+":
            result = result + int(addition_opperations[counter + 1])
        elif value == "-":
            result = result - int(addition_opperations[counter + 1])

    return result


print add_string(one)
print add_string(two)
print add_string(three)