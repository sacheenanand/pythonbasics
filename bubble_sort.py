# To sort an array from ascending order

list = [12, 11, 232 ,45,656,67]

def bubble_sort(list):
	for j in range(0, len(list)-1):
		for i in range(0, len(list)-1):
			if list[i] > list[i+1]:
				swap = list[i]
				list[i]=list[i+1]
				list[i+1]=swap
	return list
print("here is the sorted list",bubble_sort(list))
