#     1-Display stock purchase history
#     2-Exit
#     Option 1 calls the stock_purchase_history function.
#     Option 3 exits the program

from question_d import stock_purchase_history


def main():
    while True:
        print("\nMenu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            stock_purchase_history()
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Try Again.")


main()