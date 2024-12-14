#write functions here, don't add input('') statements here!
def test_config():
    return True

#-Create a create_mulitiplication_table function that returns a list.
def create_multiplication_table():
    table = []

    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i*j)
        table.append(row)
    return table

#Create a display_multiplication_table that displays a table and accepts a list parameter
def display_multiplication_table(table):
    for row in table:
        print(" ".join(str(value) for value in row))
