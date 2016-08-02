games = [('Wii Fit', 2007), ('Minecraft', 2012), ('Pac-Man', 1982)]
for g in games:
	print g[0], "maps to", g[1]

def lookup(assocs, key):
	for a in assocs:
		if a[0]==key:
			return a[1]
	return None

print lookup(games, "Minecraft")


print
games = {'Wii Fit':2007, 'Minecraft':2012, 'Pac-Man':1982}
for name in games.keys():
	print name, "maps to", games[name]
for date in games.values():
	print date
for assoc in games.items():
	print assoc # tuple

print
phones = {}
phones["parrt"] = [5707, [3, 4], 4432]
print phones
del phones["parrt"]
print phones

names = ['Pac-Man', 'Wii Fit', 'Minecraft']
dates = [1982, 2007, 2012]
games = {}
for i in range(len(names)):
	key = names[i]
	value = dates[i]
	games[key] = value
print games
print dict(zip(names, dates))