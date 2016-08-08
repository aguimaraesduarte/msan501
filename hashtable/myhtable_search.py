# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    table = htable(4011)

    index = 0
    for f in files:
        text = get_text(f)
        wordlist = set(words(text))
        for word in wordlist:
            if htable_get(table, word) == None:
                htable_put(table, word, set([index]))
            else:
                htable_put(table, word, index)
        index += 1

    return table


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    return_indices = set([])
    search_terms = set(terms)
    return_files = []

    for term in search_terms:
        if htable_get(index, term) != None:
            if len(return_indices) == 0:
                return_indices = htable_get(index, term)
            else:
                return_indices = return_indices & htable_get(index, term)

    return_indices = list(return_indices)
    for i in return_indices:
        return_files.append(files[i])

    return return_files
