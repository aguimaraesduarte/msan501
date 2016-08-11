# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    return_files = set([])
    search_terms = set(terms)

    for f in files:
    	text = get_text(f)
    	wordlist = set(words(text))
    	if len(wordlist & search_terms) == len(terms):
    		return_files.add(f)

    return list(return_files)
