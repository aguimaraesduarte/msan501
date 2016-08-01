a = ['dog', 'cat', 'dog', 'dog']
s = set(a)
for x in s: print x

print
s = "It was the best of times it was the worst of times"
wordlist = s.split(" ")
words = set(wordlist)
print words

print
words = set(w.lower() for w in words)
print words

print
words.add("dog")
print "dog" in words
print "foo" not in words
print "it" in words

print
dogs = set(['fido','fuzzy'])
cats = set(['fuzzy','bonkers'])
print dogs & cats      # set(['fuzzy'])
print dogs | cats      # set(['fuzzy', 'fido', 'bonkers'])
print len(dogs | cats) # 3

print
s1 = "It is better to burn out than to fade away"
s2 = "How many ears must one man have before he can hear people cry"

def str2words(s):
	wordlist = s.split(" ")
	words = set(wordlist)
	words = set(w.lower() for w in words)
	return words

def findCommon(w1, w2):
	return words_s1 & words_s2

words_s1 = str2words(s1)
words_s2 = str2words(s2)

print findCommon(words_s1, words_s2)