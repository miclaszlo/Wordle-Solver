import requests
import re

"""
Function Name           : fetch_five_letter_words
Author                  : Michael Laszlo
Date                    : April 11th, 2022
Function Description    : This function uses meaningpedia to fetch all of the
five letter words in the English dictionary. This function was found on GitHub
at https://gist.github.com/iancward/eaa4727a5058db51135977444655ca40.

BEGIN fetch_five_letter_words
    Print message telling User words are being fetched
    Get list of five-letter words from meaningpedia.com
    Compile regex
    Find all matches
    Return word list
END fetch_five_letter_words
"""
def fetch_five_letter_words():

    # Get all five-letter words (source: https://gist.github.com/iancward/eaa4727a5058db51135977444655ca40)
    print('Fetching word list...\n')

    # get list of five-letter words from meaningpedia.com
    # found it linked from Wikipedia:
    # https://en.wikipedia.org/wiki/Lists_of_English_words#External_links
    meaningpedia_resp = requests.get(
        "https://meaningpedia.com/5-letter-words?show=all")
    
    # compile regex
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')

    # find all matches
    word_list = pattern.findall(meaningpedia_resp.text)

    # Return word_list
    return word_list