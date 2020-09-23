# 7kyu - Isograms
# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# My Code

def is_isogram(string):

    counter = 0

    for letter1 in string:
        for letter2 in string:
            if letter1.lower() == letter2.lower():
                counter += 1
                if counter > 1:
                    return False 
        counter = 0
    return True    

is_isogram("Dermatoglyphics" )
is_isogram("aba" )
is_isogram("moOse" )


# Better Code
#
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))

