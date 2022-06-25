import random
import charactercountgraph
"""Randomly Generates a password containing Aa, numbers and symbols
Calls charactercountgraph.py to plot a graph of the most repeated characters"""

"""ERRORS"""
ERROR_INVALID_NUMBER_MESSAGE = "This is not a valid number. Try again!"

"""MESSAGES"""
INSERT_NUMBER_MESSAGE = "Insert Password Length: "

"""CHARACTER TYPES ALLOWED"""
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
BETA = ALPHA.lower()
NUM = "0123456789"
SYM = "\ !@#$%^&*()_+=-[]{};':,./<>?|`~\""
ALL = ALPHA + BETA + NUM + SYM

"""FILE NAMES"""
OUTPUT_FILENAME = "password.txt"

""""FUNCTIONS
 - Asks the user a password length, exports a randomly generated password as a text file, plots a graph"""
def main():
    password_len = ask_for_n(INSERT_NUMBER_MESSAGE)
    top_len = len(ALL)
    generated_pass = ""
    for i in range(password_len):
        generated_pass = generated_pass + ALL[random.randint(0, top_len - 1)]
    try:
        with open(OUTPUT_FILENAME, "w") as file:
            file.write(generated_pass)
    except OSError:
        print("OSError opening file.")
        exit(1)
    count_characters_and_plot_graph(OUTPUT_FILENAME, password_len)


""" - Asks the user for the password length"""
def ask_for_n(msg):
    try:
        n = int(input(msg))
        if n > 0:
            return n
        else:
            print(ERROR_INVALID_NUMBER_MESSAGE)
            return ask_for_n(msg)
    except ValueError:
        print(ERROR_INVALID_NUMBER_MESSAGE)
        return ask_for_n(msg)


""" - Counts characters and plots a bar graph for every appearance"""
def count_characters_and_plot_graph(filename, n):
    charactercountgraph.main(filename, n)


"""RUN PROGRAM"""
if __name__ == '__main__':
    main()
