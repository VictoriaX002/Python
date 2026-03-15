import Menu_Functions as lf
user_choice = 0
while user_choice != 9:
    lf.menu()
    print()
    user_choice = int(input("Please enter a menu option: "))
    if user_choice == 1:
        user_num_1 = int(input("Please enter the first number: "))
        user_num_2 = int(input("Please enter the second number: "))
        lf.menu_1(user_num_1,user_num_2)
        print()
    elif user_choice == 2:
        user_num_1 = int(input("Please enter the first number: "))
        user_num_2 = int(input("Please enter the second number: "))
        lf.menu_2(user_num_1,user_num_2)
        print()
    elif user_choice == 3:
        user_num_1 = int(input("Please enter the first number: "))
        user_num_2 = int(input("Please enter the second number: "))
        lf.menu_3(user_num_1,user_num_2)
        print()
    elif user_choice == 4:
        user_num_1 = int(input("Please enter the first number: "))
        user_num_2 = int(input("Please enter the second number: "))
        lf.menu_4(user_num_1,user_num_2)
        print()
    elif user_choice == 5:
        user_num = int(input("Please enter the first number: "))
        user_num_power = int(input("Please enter the number that the first number is raised to: "))
        lf.menu_5(user_num, user_num_power)
        print()
    elif user_choice == 6:
        user_num_1 = int(input("Please enter the start of the range:"))
        user_num_2 = int(input("Please enter the end of the range:  "))
        lf.menu_6(user_num_1,user_num_2)
        print()
    elif user_choice == 7:
        user_string = input("Please enter a string: ")
        lf.menu_7(user_string)
        print()
    elif user_choice == 8:
        user_string = input("Please enter a string: ")
        user_num = int(input("Please enter the value of the element you wish to display: "))
        while user_num <= 0 or user_num > len(user_string):
            print("Value outside of range")
            user_num = int(input("Please enter a valid value of the element you wish to display: "))
        lf.display_element(user_string,user_num)
        print()
    elif user_choice == 9:
        print("Exiting Program")




