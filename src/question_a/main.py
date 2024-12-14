
from question_a import create_multiplication_table
from question_a import display_multiplication_table


def main ():
    while True:
        multiplication_table = create_multiplication_table()

        display_multiplication_table(multiplication_table)

        user_input = input("Would you like to continue? (y/n): ").strip().lower()

        if user_input == 'n':
            print("Exiting Now")
            break

main()