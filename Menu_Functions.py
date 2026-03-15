
def menu():
    print("****************************")
    print("* Calculator + *")
    print("1- Add")
    print("2- Subtraction")
    print("3- Multiplication")
    print("4- Division")
    print("5- Raise to the power")
    print("6- List of squares")
    print("7- Upper and Lower Case")
    print("8- Display specific element")
    print("9- Exit")
    print("****************************")

def menu_1(num1,num2):
    result = num1 + num2
    print(num1, "+",num2,"is equal to", result)

def menu_2(num1,num2):
    result = num1 - num2
    print(num1, "-",num2,"is equal to", result)

def menu_3(num1,num2):
    result = num1 * num2
    print(num1, "*",num2,"is equal to", result)

def menu_4(num1,num2):
    result = num1 / num2
    print(num1, "/",num2,"is equal to", result)

def menu_5(num,power):
    result = num ** power
    print(num, "raised to", power, "is equal to", result)

def menu_6(start_in,end_in):
    for num in range(start_in, end_in+1):
        print(num*num)

def menu_7(string_in):
    num_of_upper = 0
    num_of_lower = 0
    for character in string_in:
        if character.isupper():
            num_of_upper += 1
        elif character.islower():
            num_of_lower += 1
    print("Original String: ", string_in)
    print("Number of upper case characters: ",num_of_upper)
    print("Number of lower case characters: ",num_of_upper)

def display_element(string_in,num_in):
    print("Character", string_in[num_in-1])
