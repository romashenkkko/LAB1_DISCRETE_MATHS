def generate_binary_numbers(n, binary_number=""):
    binary_numbers = []
    if n == 0:
        binary_numbers.append([int(digit) for digit in binary_number])
    else:
        binary_numbers.extend(generate_binary_numbers(n - 1, binary_number + "0"))
        binary_numbers.extend(generate_binary_numbers(n - 1, binary_number + "1"))
    return binary_numbers


def generate_value(value):
    temp = value[0]
    if len(value) != 1:
        value.remove(value[0])
    return temp


expression = input("Enter your expressions:")

variable = []
operator = []
for x in expression:
    if x >= 'a' and x <= 'z':
        variable.append(x)
    else:
        operator.append(x)

unique_variable = []
for x in variable:
    if x not in unique_variable:
        unique_variable.append(x)

for x in unique_variable:
    print(x, " | ", end="")
print(expression)
print("------------------------------------------------------------------")

values = generate_binary_numbers(len(unique_variable))

for i in range(2**len(unique_variable)):
    temp_value = []
    val = generate_value(values)
    for x in val:
        print(x, " | ", end="")
    for j in range(len(variable)):
        for i in range(len(val)):
            if variable[j] == unique_variable[i]:
                temp_value.append(val[i])

    string = ''
    j = 0

    for i in range(len(expression)):
        if expression[i] in operator:
            if expression[i] == '(':
                string = string + '('
            elif expression[i] == '!':
                string = string + ' not '
            elif expression[i] ==  ')':
                string = string + ')'
            elif expression[i] ==  '+':
                string = string + ' or '
            elif expression[i] == '*':
                string = string + ' and '

        if expression[i] in variable:
            s = str(temp_value[j])
            string = string + s
            j += 1
    if eval(string):
        print("True")
    else:
        print("False")
