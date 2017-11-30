# Author: Swetha KrishnamurthyRao
# UBID: 1004265
# This program generates all the permutations of letters in a word including uppercase and lowercase.

# Permutations functons that takes the input word and generates all possible combinations of the word recursively
def permutations(input_word):
    word = set([input_word])
    final_list = list()
    # If the length of the word is 2 then return the combination to the final list
    if len(input_word) == 2:
        word.add(input_word[1] + input_word[0])
        final_list = list(word)
    # If the length of the word is greater than 2 then call looping_through method
    elif len(input_word) > 2:
        final_list = looping_through(word, input_word)
    return final_list

# This method loops through the word and for each word generates a combination words and does this recursively.
def looping_through(word, input_word_new):
    for count, letter in enumerate(input_word_new):
        for letters in permutations(input_word_new[:count] + input_word_new[count + 1:]):
            word.add(letter + letters)

    return list(word)

# While loop recursively asks for user input
while True:
    value = input("Enter the word to calculate permutations: ")
    # If no word is entered then display an error message.
    if len(value) == 0:
        print("Please enter a valid word to generate permutations.")
    elif len(value) == 1:
        print("Permutations of the word: " + value)
    else:
        # For the entered value get the list of possible combinations and print them
        l1 = permutations(value)
        print("Permutations of the word :")
        print("-------------------------- \n")
        print(l1)
        # For uppercase and lowercase combination. Divide the word into two combinations and convert one half to uppercase and other
        # to lowercase and vice versa.
        firstLength = int(len(value) / 2)
        onePart = (value[0:firstLength]).upper() + value[firstLength:len(value)]
        secondPart = value[0:firstLength] + (value[firstLength:len(value)]).upper()
        # Call the permutations method to generate the uppercase and lowercase combinations
        l2 = permutations(onePart)
        l3 = permutations(secondPart)
        l2.append(l3)
        # Print the output
        print("Permutations of uppercase and lowercase alone:")
        print("---------------------------------------------\n")
        print(l2)


