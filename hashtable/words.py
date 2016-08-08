import os
import re
import string


def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    files = []
    for dirname, dirnames, filenames in os.walk(root):
        for filename in filenames:
            files.append(os.path.join(dirname, filename))
    return files


def get_text(fileName):
    f = open(fileName)
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    reg = re.compile('[%s]' % (string.punctuation + "0-9\\r\\t\\n\\x80\\x82\\xe2\\x94\\x99\\xc3\\xa2\\xad\\x9c\\x9d\\xa0"))
    st = reg.sub(" ", text)
    words = st.split(" ")
    words = set(words)
    words = [w.lower() for w in words if len(w) >= 3]
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    if len(docs) > 100:
        docs = docs[:100]

    num_files = len(docs)
    str_terms = " ".join(terms)

    template_start = """
    <html>
        <head>
            <title>Search results for %s in %d files</title>
        </head>

        <body>
            <h2>Search results for <b>%s</b> in <b>%d</b> files</h2>

    """

    template_end = """

        </body>
    </html>
    """

    template_result = """
    
    <br><a href="file://%s">"%s"</a><br>
    %s
    <br>

    """

    html = template_start % (str_terms, num_files, str_terms, num_files)

    for doc in docs:
        text = get_text(doc)
        text = re.sub('\ +', ' ', text).strip()
        lines = text.split("\n")
        lines = [line for line in lines if len(line) > 2]
        matching = [s for s in lines if terms[0] in s.lower()]
        indexOfFirstMatch = lines.index(matching[0])
        toPrint = "<br>".join(lines[indexOfFirstMatch:indexOfFirstMatch+2]) # first two non-empty lines of text with the first search term

        html += template_result % (doc, doc, toPrint)

    html += template_end

    return html


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

