"""
Function Name           : best_next_search
Author                  : Michael Laszlo
Date                    : April 11th, 2022
Function Description    : Given a lists of words, the word with the most 
distinct/unique letters is returned. This can be considered the 'best' guess
in Wordle as it allows the User to determine more information about the puzzle
and help further reduce the number of possible solutions/recommended guesses
provided by the program.

BEGIN best_next_search
    Initialize num_distinct to 0
    Initialize highest_num_distinct to 0
    Initialize max_num_distinct to 5
    Initialize result to an empty String
    FOR word in passed in word list
        Create set with the charcters of the word
        Set num_distinct to length of word_set
        IF num_distinct is greater than highest_num_distinct
            Set highest_num_distinct to num_distinct
            Set result to word
        ENDIF num_distinct is greater than highest_num_distinct
        IF num_distinct is equal to max_num_distinct
            Return word
        ENDIF num_distinct is equal to max_num_distinct
    END word in passed in word list
    Return result
END best_next_search
"""
def best_next_search(word_list: list):

    # Initialize num_distinct to 0
    num_distinct = 0

    # Initialize highest_num_distinct
    highest_num_distinct = 0

    # Initialize max_num_distinct to 5
    max_num_distinct = 5

    # Initialize return value
    result = ""

    # For every word in word_list
    for word in word_list:

        # Create set with the charcters of the word
        word_set = set(word)

        # Set num_distinct to length of word_set
        num_distinct = len(word_set)

        # If num_distinct is greater than highest_num_distinct
        if(num_distinct > highest_num_distinct):

            # Set highest_num_distinct to num_distinct
            highest_num_distinct = num_distinct

            # Set result to word
            result = word

        # If num_distinct is equal to max_num_distinct
        if(num_distinct == max_num_distinct):

            # Return word 
            return word

    # Return result
    return result