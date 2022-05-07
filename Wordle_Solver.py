# Import function code from other files in the directory
from Fetch_Words import fetch_five_letter_words
from Filter_Invalid import filter_invalid
from Filter_Valid import filter_valid
from Filter_Wrong_Spot import filter_wrong_spot
from Best_Next_Search import best_next_search

"""
Function Name           : main
Author                  : Michael Laszlo
Date                    : April 11th, 2022
Function Description    : The main function operates as the main interface 
between the User and the Wordle Solver. The program starts by welcoming the
User to the program and then calls fetch_five_letter_words to get a list of 
all the five letter words that are used for Wordle. Each word in the initial
word list is then added to a new list where all the words are changed to be 
all lowercase as some words from fetch_five_letter_words come back in all CAPS
for whatever reason. The User is then prompted for their last guess of the 
Wordle they are trying to solve, and the validity of each character in their
guess, with the following being the breakdown of validities:

-1 -> Letter not present in Wordle Solution
 0 -> Letter present in Wordle Solution, but in wrong spot
 1 -> Letter present in Worlde Solution and in correct spot

 The User's guess is then sent to each of the filtering methods depending on
 the validity of each letter, reducing the number of valid words in the word
 list, narrowing down a solution. After the word list has been filtered, the
 program finds a word in the word list with the highest number of distinct 
 characters and recommends that the User guess that word next to find the 
 Wordle solution fastest. The process of prompting the User for thier last 
 guess and letter validities continues until the User enters validities of 1
 for each character, indicating to the program that the User successfully
 solved the Wordle Puzzle for the day and prints a message to the User. 

BEGIN main
    Print message to the User
    Call fetch_all to get all words
    Inititalize word_list to an empty list
    Ensure that every word in the initial_word_list is lower case
    Initialize guess to an empty string
    Intitialize valid list
    Initialize solution list
    Initialize guess_count to 0
    WHILE User has not used all their guesses
        Prompt User for their guess
        Prompt User for the validity of each letter they guessed
        IF valid equals sol
            Print message
        END IF valid equals sol
        Initialize valid_index to 0
        Iterate through valid to see if there are words we can remove from the word_list
        Print suggestions to User for their next guess
        Increment guess_count
    END WHILE User has not used all their guesses
END main
"""

# Main function
def main():

    # Print message to the User
    print("\nWelcome to Wordle_Solver! Note: Wordle_Solver is not perfect, but program will make solving the Worlde that much easier! Good luck!\n")

    # Call fetch_all to get all words
    initial_word_list = fetch_five_letter_words()

    # Inititalize word_list to an empty list
    word_list = []

    # Ensure that every word in the initial_word_list is lower case
    for word in initial_word_list:

        # Add word to word_list
        word_list.append(str.lower(word))

    # Initialize guess to an empty string
    guess = ""

    # Intitialize valid list
    valid = [-1, -1, -1, -1, -1]

    # Initialize solution list
    sol = [1, 1, 1, 1, 1]

    # Initialize guess_count to 0
    guess_count = 0

    # While User has not used all their guesses
    while(guess_count < 6):

        # Prompt User for their guess
        guess = str.lower(input("What was your last guess?: "))

        # Prompt User for the validity of each letter they guessed
        print("For entering validity of each character in your guess use the following: ")
        print("-1 -> Letter is not in the puzzle")
        print("0 -> Letter is in the puzzle but in the wrong spot")
        print("1 -> Letter is in the puzzle and in the correct location\n")
        valid[0] = int(input("Enter validity of first letter: "))
        valid[1] = int(input("Enter validity of second letter: "))
        valid[2] = int(input("Enter validity of third letter: "))
        valid[3] = int(input("Enter validity of fourth letter: "))
        valid[4] = int(input("Enter validity of fifth letter: "))

        # If valid equals sol
        if(valid == sol):

            # Print message
            print("\nCongrats, you solved today's Wordle!")
            return None

        # Initialize valid_index to 0
        valid_index = 0

        # Iterate through valid to see if there are words we can remove from the word_list
        for entry in valid:

            # If entry is -1
            if(entry == -1):

                # Call filter_invalid function to remove any words contain the letter 
                word_list = filter_invalid(word_list, guess[valid_index])

            # If entry is 0
            if(entry == 0):

                # Call filter_wrong_spot
                word_list = filter_wrong_spot(guess[valid_index], valid_index, word_list)

            # If entry is 1
            if(entry == 1):

                # Call filter_valid
                word_list = filter_valid(guess[valid_index], valid_index, word_list)

            # Increment valid_index
            valid_index = valid_index + 1

        # Print suggestions to User for their next guess
        print("\nAll suggestions for your next guess:")
        print(word_list)
        print("\nRecommended next guess:")
        print(best_next_search(word_list))
        print()

        # Increment guess_count
        guess_count = guess_count + 1


# Run main
if __name__ == "__main__":

    main()