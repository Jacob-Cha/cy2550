#!/usr/bin/env python3
import random
import argparse

# Define an argument parser for command line arguments
parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method')
parser.add_argument('-w', '--words', type=int, default=4,
                    help='include WORDS words in the password (default=4)')
parser.add_argument('-c', '--caps', type=int, default=0,
                    help='capitalize the first letter of CAPS random words (default=0)')
parser.add_argument('-n', '--numbers', type=int, default=0,
                    help='insert NUMBERS random numbers in the password (default=0)')
parser.add_argument('-s', '--symbols', type=int, default=0,
                    help='insert SYMBOLS random symbols in the password (default=0)')
args = parser.parse_args()

# Load a word list from a file
with open('words.txt') as f:
    wordlist = [word.strip() for word in f]

# Choose a subset of words from the word list
words = random.sample(wordlist, args.words)

# Capitalize random words
if args.caps > 0:
    caps = random.sample(range(args.words), args.caps)
    words = [w.capitalize() if i in caps else w for i, w in enumerate(words)]

# Insert random numbers
if args.numbers > 0:
    for i in range(args.numbers):
        words.insert(random.randint(0, len(words)), str(random.randint(0, 9)))

# Insert random symbols
if args.symbols > 0:
    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '.', ':', ';']
    for i in range(args.symbols):
        words.insert(random.randint(0, len(words)), random.choice(symbols))

# Join the words and symbols to form the password
password = ''.join(words)

# Print the password to the console
print(password)