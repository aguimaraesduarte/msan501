from collections import defaultdict  # https://docs.python.org/2/library/collections.html
from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document indexes. The document index is just the index into the
    files parameter (indexed from 0).
    Make sure that you are mapping a word to a set, not a list.
    For each word w in file i, add i to the set of documents containing w
    Returns a dict object.
    """
    return_dict = {}

    index = 0
    for f in files:
        text = get_text(f)
        wordlist = set(words(text))
        for word in wordlist:
            if word not in return_dict:
                return_dict[word] = set([index])
            else:
                return_dict[word].add(index)
        index += 1

    return return_dict


def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files and look inside.
    """
    return_indices = set([])
    search_terms = set(terms)
    return_files = []

    for term in search_terms:
        if term in index.keys():
            if len(return_indices) == 0:
                return_indices = index[term]
            else:
                return_indices = return_indices & index[term]

    return_indices = list(return_indices)
    for i in return_indices:
        return_files.append(files[i])

    return return_files