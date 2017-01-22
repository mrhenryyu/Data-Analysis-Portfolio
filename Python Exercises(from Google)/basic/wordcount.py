#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def print_words(filename):
  # store all of the words in a list, sort the list
  # get all of the files in a list, then have a key - value pair dictionary
  # make them all lower case 
# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

  d = read_file(filename)
  print d
def print_top(filename):
  ## same thing as print_words, but only with the top 20 words
  d = read_file(filename)
  for item in d[:20]:
    print item[0], item[1]

def get_count(word_count_tuple):
  """Returns the count from a dict word/count tuple  -- used for custom sort."""
  return word_count_tuple[1]

def read_file(filename):
  #open file, read file, and store all words present in a list 
  f = open(filename, 'rU')
  input_s = f.read()
  input_l = input_s.lower()
  words = input_l.split()
  #next, create a dictionary and add each word and its frequency to it
  #sort the dictionary by the value 
  word_bank = {}
  for word in words:
    if word in word_bank: # if the word is already present in the dictionary
      #word_bank.get(word)was the previous one
      word_bank[word] = word_bank[word] + 1 
    else: # else, if the word is NOT already present in the dictionary 
      word_bank[word] = 1

  f.close()
  bank = sorted(word_bank.items(), key=get_count, reverse=True)
  return bank


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
