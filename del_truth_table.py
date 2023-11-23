#and = +, or = *, not = !

import prettytable
elements_dict = {}
user_input = input("Enter your logical statement: ")
splited_user_input = [str(element) for element in str(user_input)]
print(splited_user_input)

for element in splited_user_input:
    if element.isalpha():
        elements_dict[element] = []
print(elements_dict)

expression = [element for element in splited_user_input if not element.isalpha()]

print("Original input:", splited_user_input)
print("Expression without alphabet characters:", expression)

length = len(elements_dict)
num_combinations = 2**length

for i in range(num_combinations):
    binary = f'{i:0{length}b}'
    bin = str(binary)
    j = 0
    for key in elements_dict:
        elements_dict[key].append(int(bin[j]))
        j += 1
print(elements_dict)

expression = list(map(lambda x: x.replace('+', 'AND'), expression))
expression = list(map(lambda x: x.replace("*", "OR"), expression))
expression = list(map(lambda x: x.replace("!", "NOT"), expression))



