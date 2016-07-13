
# import function called choice from module random
from random import choice

user_n_gram = 3 #int(raw_input("State the n size of your n-gram: "))

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
    
    for i in range(len(words) - (user_n_gram + 1)):
        # make this a list by enclosing in []
        n_gram = [words[i]]     
        for n in range(1,user_n_gram):
            n_gram.append(words[i+n])  
        #convert list into tuple for dictionary key
        n_gram_tuple = tuple(n_gram)
        chain_dictionary[n_gram_tuple] = []

    print len(words)

    # loop through once!!
    for i in range(len(words) - (user_n_gram) - 1):
        n_gram = [words[i]]     
        for n in range(1,user_n_gram):
            n_gram.append(words[i+n]) 
        n_plus_word = words[i+user_n_gram]
        n_gram_tuple = tuple(n_gram)
        chain_dictionary[n_gram_tuple].append(n_plus_word)

    # appending None to last bi-gram in our dictionary
    # chain_dictionary[(words[-2], words[-1])].append(None)

    print chain_dictionary

make_chains(open_and_read_file("green-eggs.txt"))

# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     my_list = []

#     #create initial bi_gram by randomly selecting a key 
#     bi_gram = choice(chains.keys())

#     #randomly select a value for initial bi_gram
#     third_word = choice(chains[bi_gram])
#     # use extend for long string of items converted into a list
#     my_list.extend([bi_gram[0], bi_gram[1], third_word])

#     while third_word != None:
#         bi_gram = (my_list[-2],my_list[-1])
#         third_word = choice(chains[bi_gram])
#         my_list.append(third_word)

#     #strip None from the end of the list
#     del my_list[-1]    

#     #create a string from from the list
#     return " ".join(my_list)

# #assign file name to input path
# #input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(file_name)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text

