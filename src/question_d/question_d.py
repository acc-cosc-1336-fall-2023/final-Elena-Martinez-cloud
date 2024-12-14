#1-Create a class Stock with private variables symbol and company_name. (Create a constructor
#  that accepts symbol and company_name)
#2-Create a stock class function/method that returns symbol
#3-Create a stock class function/method that returns company_name
#4-Create a function stock_purchase_history.
#   a-Create 5 variables/instances of Stock with the values from the Stock List table above
#  (AAP, CAT etc)
#   b-Add the 5 stock variables to a dictionary
#   c-Loop through the dictionary to display the list as displayed above in the table
def test_config():
    return True

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def stock_purchase_history():
    stock1 = Stock("AAPL", "Apple Inc.")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    stocks = {
        stock1.get_symbol(): stock1,
        stock2.get_symbol(): stock2,
        stock3.get_symbol(): stock3,
        stock4.get_symbol(): stock4,
        stock5.get_symbol(): stock5
    }

    print("\nStock Purchase History:")
    print(f"{'Company':<20}{'Symbol'}")
    print("-"*30)
    for symbol, stock in stocks.items():
        print(f"{stock.get_company_name():<20}{symbol}")