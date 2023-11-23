def input_checker():
    while True:
        input_number = input("Enter a POSITIVE NATURAL NUMBER: ")
        try:
            number = int(input_number)
            if number > 0:
                print("Your integer number is: ", number)
                break
            else:
                print("It is not POSITIVE int, try again")
        except ValueError:
            print("It is not an integer, try again")
            continue
    return number


number = input_checker()

input_number_digits = [int(digit) for digit in str(number)]
print(input_number_digits)

predecessors = []

for element in range(number - 1, 0, -1):
    predecessors.append(element)
    predecessors_sorted = sorted([int(digit) for digit in str(element)])
    if predecessors_sorted == sorted(input_number_digits):
        print(f"The smallest num of n digits is: {element}")
        break
