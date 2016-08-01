'''
f = open("filename", "r")
for row in f:
	row = row.strip()
	cols = row.split(" ")
	print cols
f.close()
'''

s = """
Dogs have masters
Cats have staff
Bonkers and booboo
"""
lines = s.strip().split("\n")
print lines
#words = []
#for line in lines:
#	words += lines.split(" ")

words = [line.split(" ") for line in lines]
print words