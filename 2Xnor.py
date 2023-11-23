# demo version of an automatic checker

def input_checker():
    while True:
        first_value = input("Enter first_value true, false, 1, or 0: ")
        if first_value.lower() not in ('false', 'true', '0', '1'):
            print("Not an appropriate choice.")
            continue
        else:
            break
    while True:
        second_value = input("Enter second_value true, false, 1, or 0: ")
        if second_value.lower() not in ('false', 'true', '0', '1'):
            print("Not an appropriate choice.")
            continue
        else:
            break
    return first_value, second_value

def perform_xnor(first_value, second_value):
    first_value = first_value.lower() == 'true' or first_value == '1'
    second_value = second_value.lower() == 'true' or second_value == '1'

    result = first_value == second_value
    print(result)

first_value, second_value = input_checker()
perform_xnor(first_value, second_value)
