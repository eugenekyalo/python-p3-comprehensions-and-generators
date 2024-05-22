# lib/list_comprehension.py

def return_evens(lst):
    return [n for n in lst if n % 2 == 0]

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]
