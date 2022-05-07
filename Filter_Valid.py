"""
Function Name           : filter_valid
Author                  : Michael Laszlo
Date                    : April 11th, 2022
Function Description    : This function takes in a word list, a letter, and 
letter position as it's arguments. This function is called when the User has
specified a letter that is in the correct position of the Wordle puzzle they 
are solving. Because this letter is in the correct position, we can remove
and words from the word list that do not have the letter specified by the User
in the correct position.

BEGIN filter_valid
    Initialize empty return list
    FOR every word in word_list
        IF word[valid_pos] is equal to letter specified by the User
        Add word to return_list
        ENDIF word[valid_pos] is equal to letter specified by the User
    ENDFOR every word in word_list
    Return return list
END filter_valid
"""
def filter_valid(letter: str, valid_pos: int, word_list: list):

    # Initialize empty return list
    return_list = []

    # For every word in word_list
    for word in word_list:

        # If word[valid_pos] is equal to letter specified by the User
        if(word[valid_pos] == letter):

            # Add word to return_list
            return_list.append(word)

    # Return return_list
    return return_list