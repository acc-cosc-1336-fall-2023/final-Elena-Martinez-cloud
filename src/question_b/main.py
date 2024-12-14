from question_b import display_stock_history, get_stock_list

#The program continues until the user opts out. Create a main function, 
#Call the get_stock_list and save the return value to a variable.
#Create the following menu:
#     1-Display stock purchase history
#     2-Exit
#     Option 1 calls the stock_list function and displays the data from the list.
#     Option 2 exits the program#

def main():
    stock_list = get_stock_list()

    while True:
        print("\Menu:")
        print("1 - Display stock purchase history")
        print("2 - Exit")

        choice = input("Please choose 1 or 2: ")

        if choice == "1":
            display_stock_history(stock_list)
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid! Please choose from 1 or 2.")

main ()