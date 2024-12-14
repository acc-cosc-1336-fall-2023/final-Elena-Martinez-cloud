#Create a Stock class with one constructor with symbol and company_name parameters, 
#private attributes(variables) symbol and company_name, and public functions get_symbol and 
#get_company_name.

class Stock:
    def __init__(self, symbol, company_name):
        
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    

#Create a function get_stock_list - create 5 Stock class instance variables/objects
def get_stock_list():
    stock1 = Stock("APPL", "Apple Inc.")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")


#Add them to a list, return the list.
    stock_list = [stock1, stock2, stock3, stock4, stock5]
    return stock_list

def display_stock_history(stock_list):
    for stock in stock_list:
        print(f"Symbol: {stock.get_symbol()}   Company: {stock.get_company_name()}")