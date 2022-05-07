"""
Function Name           : filter_invalid
Author                  : Michael Laszlo
Date                    : April 11th, 2022
Function Description    : This function takes in a list of words and a letter
as it's arguments. This function is called when the User has specified that a
letter is not present in the Wordle puzzle they are solving. Because we know
any word containing this character cannot solve the Wordle, we create a
return list with any words from the passed in word list containing the invalid
letter not present.

BEGIN filter_invalid
    Initialize an empty list to hold valid words
    FOR each word in the word_list
        IF word does not contain the letter
            Add word to return_list
        ENDIF word does not contain the letter
    ENDFOR each word in the word_list
    Return return_list
END filter_invalid
"""
def filter_invalid(word_list: list, letter: str ):
    
    # Initialize an empty list to hold valid words
    return_list = []

    # For each word in the word_list
    for word in word_list:

        # If word does not contain the letter
        if(letter not in word):

            # Add word to return_list
            return_list.append(word)

    # Return return_list
    return return_list