"""
File: anagram.py
Name: Ching-Tsung Tsai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
ALL_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Global variable
dict_lst = []                 # save all the words in dictionary.txt as a dictionary
dict_dct = {}
count = [0]                   # count recursion times
current_index = [0]           # the current index of the last word being searched in has_prefix_extension
alphabet_idx = {}             # save the index of the alphabets in a lst


def main():
    """
    Goal: find all anagrams of the input letter
    """
    global current_index
    read_dictionary()
    read_alphabet()
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    while True:
        word = input("Find anagrams for: ").lower()
        start = time.time()
        if word != EXIT:
            count[0] = 0
            find_anagrams(word)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')
            current_index = [0]                                                 # clear the index of the previous word
        else:
            break


def read_alphabet():
    """
    This function save the 1st index of all alphabets
    The has_prefix() function can use this function to start searching from the specific alphabet
    eg. contains -> start searching from c
    """
    for a in ALL_ALPHABET:
        for i in range(len(dict_lst)):
            if dict_lst[i].startswith(a):
                if a not in alphabet_idx:
                    alphabet_idx[a] = i


def read_dictionary():
    global dict_lst
    global dict_dct
    with open(FILE, "r") as d:
        dict_dct = {line.strip(): line.strip() for line in d}
    with open(FILE, "r") as d:
        dict_lst = [line.strip() for line in d]


def find_anagrams(s):
    """
    :param s: str, the input word
    """
    s_dict = {alpha: s.count(alpha) for alpha in s}                 # count the character; eg. been-> b:1, e:2, n:1
    ans_lst = []
    helper(s_dict, ans_lst, "", len(s))              # char. dict, answers, current word, word length
    print(f"{len(ans_lst)} anagrams: {ans_lst}")
    # print(f"Recursive counts: {count}")


def helper(s_dict, ans_lst, current_word, word_len):
    """
    :param s_dict: dict, the dictionary that counted the number of characters
    :param ans_lst: list, save all the anagrams
    :param current_word: str, the word that aims to become an anagram
    :param word_len: the length of the input word
    """
    global current_index
    count[0] += 1
    if len(current_word) == word_len and current_word in dict_dct:  # Base-case
        ans_lst.append(current_word)                                # because the word may not be in the dictionary
        print(f"Found: {current_word}\nSearching...")               # even if has_prefix = True
    else:
        for alphabet in s_dict:
            if s_dict[alphabet] > 0:
                current_word += alphabet
                # if has_prefix(current_word):
                s_dict[alphabet] -= 1                           # count -1 if the char. is added in current_word
                helper(s_dict, ans_lst, current_word, word_len)
                s_dict[alphabet] += 1
                current_index = current_index[:(len(current_word))] # Un-choose, return current_index to previous state
                current_word = current_word[:-1]


def has_prefix(sub_s):
    """
    :param sub_s: str, the current word in the helper function
    :param current_index: lst, save the last index that the dictionary has run in the possible letter
    :return: bool, to examine whether there's at least a word in dictionary.txt has a prefix that is same as the input
    """
    if len(sub_s) == 1:
        current_index[0] = alphabet_idx[sub_s]                       # replace index 0 to the current prefix's 1st index
    for i, w in enumerate(dict_lst[current_index[-1]:]):
        if w.startswith(sub_s):
            current_index.append(current_index[-1]+i)                # save the index of the last word being searched
            return True
        elif len(w) >= len(sub_s) and w[len(sub_s)-1] > sub_s[-1]:   # stop looping if the last char. of w > sub_s
            return False


if __name__ == '__main__':
    main()
