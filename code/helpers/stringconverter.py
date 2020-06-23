def string_converter(string):
    """converts the string values in a protein string
    to numerical values in order to process the information"""
    
    protein_string_converted = []

    for i in range(len(string)):

        if string[i] == 'H':
            protein_string_converted.append(1)
        elif string[i] == 'P':
            protein_string_converted.append(2)
        elif string[i] == 'C':
            protein_string_converted.append(3)
    
    return protein_string_converted