#program to find rhe 
list = ["nikeee","nikkar","nikle","nike"]
def prefix(list):
	shortest_string = min(list, key=len)
	print("to check the short word in the list",shortest_string)

	for i, char in enumerate(shortest_string):

		for words in list:
			if words[i]!= char:
				return shortest_string[:i]

print("here is the prefix elemnet",prefix(list))

