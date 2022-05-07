"""
Function Name           : filter_wrong_spot
Author                  : Michael Laszlo
Date                    : April 11th, 2022
Function Description    : This function takes in a word list, a letter, and 
letter position as it's arguments. This function is called when the User 
specifies that a letter is in the Wordle puzzle they are solving, but the
letter is in the wrong spot. Because this letter is in the wrong spot, we
can remove any word from the word list that has the specified letter at that
index. 

BEGIN filter_wrong_spot
    Initialize return list
    FOR every word in word list
        IF letter at letter_pos is does not equal letter
            Add word to return_list
        END IF letter at letter_pos is does not equal letter
    END FOR every word in word list
    Return return list
END filter_wrong_spot
"""
def filter_wrong_spot(letter: str, letter_pos: int, word_list: list):

    # Initialize return list
    return_list = []

    # For every word in the list
    for word in word_list:

        # If letter at letter_pos is not letter
        if(word[letter_pos] != letter):

            # Add word to return_list
            return_list.append(word)

    # Return return list
    return return_list