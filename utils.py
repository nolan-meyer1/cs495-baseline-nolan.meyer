def slugify(s):
    """
    This function takes in a paramter s which is 
    some string. It will then make it lowercase,
    replaces spaces with dashes, and strip out
    invalid characters which is anything that is 
    not a-z,0-9, or a dash.
    """

    output = ""

    for character in s:

        if ((character.isalpha() or character.isnumeric()) or (character == " " or character == " ")):
            if character == " ":
                output += "-"
            elif not character.islower():
                output += character.lower()
            else:
                output += character
    
    return output
            

