def version1(filename):
	with open(filename) as f:
		lines = f.read().splitlines()

	combo = {}
	for line in lines:
		if line.startswith("Combo"):
			_, username, password = line.split(":")
			combo[username[1:]] = password
	return combo
