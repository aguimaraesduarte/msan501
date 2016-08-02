NBUCKETS = 7
buckets = [[] for i in range(NBUCKETS)] #create an empty list for each bucket

#here, keys are strings
def hash(key):
	return ord(key[0]) #returns the character code for the letter

def lookup(buckets, key):
	h = hash(key)
	b = h % NBUCKETS
	bucket = buckets[b]
	for assoc in bucket:
		if key == assoc[0]:
			return assoc[1]
	return None

def put(buckets, key, value):
	h = hash(key)
	b = h % NBUCKETS
	buckets[b].append((key, value))

put(buckets, "Alaska", "AK")
put(buckets, "Nevada", "NE")
put(buckets, "Oregon", "OR")

print buckets

print lookup(buckets, "Alaska")
print lookup(buckets, "Nevada")
print lookup(buckets, "Oregon")
