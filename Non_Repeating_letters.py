# Given a string find the first non repeating character in string, example : google it should return "l"


def non_repeating(string):
	count = {}
	list = []

	for i in string:
		if i not in count:
			count[i]=1
			list.append(i)
		else:
			count[i] += 1

	for k in list:
		if count[k] == 1:
			return k
	return False
print(non_repeating("google"))