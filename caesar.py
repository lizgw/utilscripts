# caesar.py
#   a script to print out all possible solutions of a
#   caesar cipher.
# v1.0 - 03/23/2019

def getShiftedLetter(letter, shift):
    # get the ascii value of the letter
    ascii_num = ord(letter)
    # figure out what the shifted number is
    new_num = ascii_num + shift

    # make sure it's still a letter, so loop if necessary
    # if it passed the range of capital letters or lowercase letters
    if (new_num > 90 and new_num < 97) or new_num > 122:
        # loop it around
        new_num -= 26

    return chr(new_num)

txtfilename = input("ENTER FILENAME: ")
# a list of all the possible decoded strings
decodedList = []
# fill it up with the starter stuff
for i in range(0, 24):
    padded_zero = ""
    if(i < 10):
        padded_zero = "0"
    decodedList.append("shifted " + padded_zero + str(i) + ": ")

with open(txtfilename, "r") as f:
    text = f.read().lower()
    # go through one letter at a time
    for letter in text:
        # add the letter (shifted the right # of times) to each decoded string
        for i in range(0, len(decodedList)):
            if letter.isalpha():
                # try decoding it
                decodedList[i] += getShiftedLetter(letter, i)
            else:
                # just add it to all the lists
                decodedList[i] += letter
    # now print all the decoded strings
    for decodedString in decodedList:
        print(decodedString)

