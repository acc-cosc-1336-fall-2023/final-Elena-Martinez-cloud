#write functions here, don't add input('') statements here!
#Create a function get_most_likely_ancestor_consensus with two string parameters dna_string1 
#and dna_string2 that returns the beginning position of occurrences of dna_string2 in dna_string1
#as multiple Python parameters (not a string or list)

def test_config():
    return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):

    positions = []

    for i in range(len(dna_string1) - len(dna_string2) + 1):
        if dna_string1 [i:i + len(dna_string2)] == dna_string2:
            positions.append(i + 1)

    return tuple(positions)

def validate_input(dna_string1, dna_string2):

    if len(dna_string1) < 9 or len(dna_string2) > 16:
        print("dna_sting1 needs to be between 9 and 16 characters.")
        return False
    
    if len(dna_string2) != 4:
        print("dna_string2 needs to be 4 characters long.")
        return False
    return True