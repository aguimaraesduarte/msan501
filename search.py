# search a tree
def search(t, name):
	if t.data == name: return True
	if search(t.left, name) or search(t.right, name): return True
	return False