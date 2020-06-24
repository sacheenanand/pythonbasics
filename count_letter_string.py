#to count how many "e" are in a givem string.


def count_e(string):
	count = 0

	for i in string:
		if i == 'e':
			count+=1
	return count
print("here is the number of times the e has appeared in string",count_e("sacheeeeeeeeeen"))
