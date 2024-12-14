#The program continues until the user opts out.
#Prompt the user for a DNA string greater than 8 characters but less than or equal to 16.
#Prompt the user for a DNA substring of exactly 4 characters.
#Validate both values, the program will not continue until the validation passes for both strings.
#Call the get_most_likely_ancestor_consensus function with the user-provided values.
#Display the result to screen.
from question_c import get_most_likely_ancestor_consensus, validate_input

def main():
    while True:

        while True:
            dna_string1 = input("Enter DNA string 9 to 16 characters long: ").upper()
            dna_string2 = input("Enter a DNA substring exactly 4 characters long: ").upper()

            if validate_input(dna_string1, dna_string2):
                break
            else:
                print("Invalid! Please try again.")

        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
        if result:
            print("Positions of substring:", *result)
        else:
            print("Nothing found.")

        cont = input("Would you like to continue? (y/n): ").strip().lower()
        if cont != "y":
            print("Exiting Now.")
            break


main()