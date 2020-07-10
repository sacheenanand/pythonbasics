# Given a list of number and key, find the index of the given key in the list

def index_numbers(list, key):
	result = []

	for i in range(len(list)):
		if list[i] == key:
			result.append(i)
	return result
print(index_numbers([1,2,3,2,3,4,5,3,4,2,9], 9))
