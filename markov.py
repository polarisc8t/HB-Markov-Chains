import sys

# import function called choice from module random
from random import choice

file_name = sys.argv[1]


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    opened_file = open(file_path)
    file_string = opened_file.read()
    opened_file.close()

    return file_string
    
def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    # words should really be words - it's a list of words (duck typing)
    # tokenizing a string of words
    words = text_string.split()
    
    chain_dictionary = {}

    #for loop to add bigrams to dictionary as keys
    # don't need a bigram of last word so we put -1 on the sensitivity list in 'for' loop
    for chain_keys in range(len(words)-1):
        # make this a tuple via making this enclosed in parentheses
        bi_gram = (words[chain_keys], words[chain_keys + 1])
        # assign to empty list
        chain_dictionary[bi_gram] = []

    # loop through once!!
    for i in range(len(words)-2):
        bi_gram = (words[i], words[i+1])
        third_word = words[i+2]
        chain_dictionary[bi_gram].append(third_word)

    # appending None to last bi-gram in our dictionary
    chain_dictionary[(words[-2], words[-1])].append(None)

    # loops through multiple times and is not as efficient as the aforementioned
    # #loop over bigrams in dictionary to grab third word
    # for key in chain_dictionary:
    #     values_list = []
    #     for chain_values in range(len(words) - 2):
    #         bi_gram = words[chain_values], words[chain_values + 1]
    #         #if bigram key is found, capture third word and add to list
    #         if key == bi_gram:
    #             bi_gram_plus_one = words[chain_values + 2]
    #             values_list.append(bi_gram_plus_one)
    #             #append new list of values to dictionary
    #             chain_dictionary[bi_gram] = values_list

    return chain_dictionary

#print make_chains(open_and_read_file("green-eggs.txt"))

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    my_list = []

    #create initial bi_gram by randomly selecting a key 
    bi_gram = choice(chains.keys())

    #randomly select a value for initial bi_gram
    third_word = choice(chains[bi_gram])
    # use extend for long string of items converted into a list
    my_list.extend([bi_gram[0], bi_gram[1], third_word])

    while third_word != None:
        bi_gram = (my_list[-2],my_list[-1])
        third_word = choice(chains[bi_gram])
        my_list.append(third_word)

    #strip None from the end of the list
    del my_list[-1]    

    #create a string from from the list
    return " ".join(my_list)

#assign file name to input path
#input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(file_name)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

