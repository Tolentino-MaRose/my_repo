import os

def clear():
    os.system('cls')

def tolentino_menu():
    while True:
        clear()
        print("==========================================")
        print("  Good Day! I'm Ma. Rose L. Tolentino. ")
        print("==========================================\n")
        print("1. Basic Info             ")
        print("2. Motivational Quotes    ")
        print("3. Exit                   \n")

        user_choice = int(input("Enter your choice: "))

        match user_choice:
            case 1:
                clear()
                print("\nAge: 20 years old.")
                print("Gender: Female.")
                print("School: PUP - Taguig.\n")
                input("Press Enter to return to the menu...")
            case 2:
                clear()
                print("\n“Keep your face always toward the sunshine—and shadows will fall behind you.” – Walt Whitman")
                print("\n“The best preparation for tomorrow is doing your best today.” – H. Jackson Brown")
                print("\n“Opportunities don't happen, you create them.” – Chris Grosser\n")
                input("Press Enter to return to the menu...")
            case 3:
                clear()
                print("Thank you for using my menu! Exiting...")
                break
            case _:
                clear()
                print("\nInvalid input! Please try again.\n")
                input("Press Enter to continue...")


tolentino_menu()
