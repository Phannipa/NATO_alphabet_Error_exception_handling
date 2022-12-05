# Code for day 29 Nato phonetic alphabet

# # TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}
#
# import pandas
#
# # Create a dataframe.
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
#
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)



# Code for day 30. Catch the KeyError whean a user enters a character that is not in the dictionary.
# Provide feedback to the user when an illegal word was entered such as the number.
# Continue prompting the user to enter another word until they enter a valid word.

import pandas

# Create a dataframe.
data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic(): # In case we want to repeat question to input the name again, we can use loop or function.
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic() # We have to call function.