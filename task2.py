def calculator():
    while True:
        print('||| Enter the operation |||')
        print('||| 1. Addition         |||')
        print('||| 2. Subtraction      |||')
        print('||| 3. Multiplication   |||')    
        print('||| 4. Division         |||')
        print('||| 5. Exit             |||')
        choice = input('Enter your choice (1 - 5): ')

        if choice == '5':
            print('||| You have exited the calculator. Thank you! |||')
            break

        if choice in ['1', '2', '3', '4']:
            try:
                first_number = float(input('Enter first number: '))
                second_number = float(input('Enter second number: '))

                if choice == '1':
                    print(f"Addition result of the numbers is {first_number + second_number}")

                elif choice == '2':
                    print(f"Subtraction result of the numbers is {first_number - second_number}")

                elif choice == '3':
                    print(f"Multiplication result of the numbers is {first_number * second_number}")

                elif choice == '4':
                    if second_number != 0:
                        print(f"Division result of the numbers is {first_number / second_number}")
                    else:
                        print('||| Error! Division by zero is not allowed |||')

            except ValueError:
                print("||| Error! Please enter valid numbers. |||")
        else: 
            print('||| Error! Invalid option. Please select a valid option (1-5). |||')

        continue_choice = input('Do you want to try the calculator again? (Yes/No): ').strip().lower()
        if continue_choice == 'no':
            print("Thank you for using the calculator!")
            break

calculator()
