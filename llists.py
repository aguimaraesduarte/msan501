'''
#users = ("parrt", ("tombu", ("afedosov", None)))
#print users

a = ["parrt", None]
b = ["tombu", None]
c = ["afedosov", None]
users = a # points to first node of list
a[1] = b  # first node's next points to 2nd element
b[1] = c
print users
# add new link
b[1] = ["mary", b[1]]
print users
# add new head
d = ["jane", None]
d[1] = users
users = d
print users


print
print
head = ["parrt", None]
print head
head = ["tombu", head]
print head
head = head[1]
print head

head2 = None
head2 = ["parrt", head2]
'''


head = None
VALUE = 0
NEXT = 1

# add x to the head of the list
def add(x):
	global head
	head = [x, head]

def deletefirst():
	global head
	if head is None:
		return
	head = head[NEXT]

def getitem(j):
	i = 0
	p = head
	while p is not None:
		#print i, p[VALUE]
		if i == j:
			return p
		i += 1
		p = p[NEXT]
	return None

def length():
	n = 0
	p = head
	while p is not None:
		n += 1
		p = p[NEXT]
	return n

def show():
	values = []
	p = head
	while p is not None:
		values.append(p[VALUE])
		p = p[NEXT]
	print str(values)

def contains(x):
	p = head
	while p is not None:
		if x == p[VALUE]:
			return True
		p = p[NEXT]
	return False


def index(x):
	i = 0
	p = head
	while p is not None:
		if x == p[VALUE]:
			return i
		i += 1
		p = p[NEXT]
	return -1

def insertafter(i, x):  # add x after ith node
	p = getitem(i)
	if p is not None:
		p[NEXT] = [x, p[NEXT]]

'''
add("Frank")
add("Parrt")
add("Xue")
show()
print length()
x = getitem(2)
print x
'''

add("parrt")
add("tombu")
add("afedosov")

show()
print "length =", length()

print "index('parrt') =", index('parrt')
print "index('tombu') =", index('tombu')
print "index('afedosov') =", index('afedosov')
print "index('foo') =", index('foo')

print "getitem(0) =", getitem(0)
print "getitem(1) =", getitem(1)
print "getitem(2) =", getitem(2)

deletefirst()
deletefirst()
show()
print "length =", length()

print contains("parrt")
print contains("foo")

insertafter(0, "jimbo")
show()
print "length =", length()