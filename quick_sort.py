#Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. 
#A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot, based on which the partition is made and 
#another array holds values greater than the pivot value.

#Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. 
#This algorithm is quite efficient for large-sized data sets as its average and worst-case complexity are O(nLogn) and image.png(n2), respectively.

#The pivot value divides the list into two parts. And recursively, we find the pivot for each sub-lists until all lists contains only one element.


list = [3,1,2,4,5,3,5,6,7,1]


def quick_sort(list, low, high):
	if low < high:
		p = partion(list, low, high)
		quick_sort(list, low, p-1)
		quick_sort(list, p+1, high)





def partion(list, low, high):
	divider = low
	pivot = high

	for i in range(low, high):
		if list[i] < list[pivot]:
			list[i], list[divider] = list[divider], list[i]
			divider +=1
	list[divider],list[pivot] = list[pivot],list[divider]
	return divider
quick_sort(list, 0, 9)

print("here you go", list)







