#merge sort
#https://en.wikipedia.org/wiki/Merge_sort


list = [9,3,2,1,3,4,5,6,7,1]
def merge(left, right, array):
	i =0
	j = 0
	k = 0

	while i<len(left) and j<len(right):
		if left[i] < right[j]:
			array[k] = left[i]
			i+=1
		else:
			array[k] = right[j]
			j+=1

		k+=1

	while i<len(left):
		array[k] = left[i]
		i+=1
		k+=1
	while j<len(right):
		array[k] = right[j]
		j+=1
		k+=1


def merge_sort(array):
	n = len(array)

	if n<2:
		return

	mid = n/2
	left = []
	right = []

	for i in range(int(mid)):
		number = array[i]
		left.append(number)

	for i in range(int(mid),int(n)):
		number = array[i]
		right.append(number)

	merge_sort(left)
	merge_sort(right)

	merge(left,right, array)

merge_sort(list)
for i in list:
	print(i)











