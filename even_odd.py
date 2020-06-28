

list = [1,2,3,4,5,6,7,8,9,10,12,13,14,16,17,18,20]

def even_odd(list):
	j = -1

	for i in range(0, len(list)):

		if list[i]%2==0:
			j= j+1
			temp = list[i]
			list[i]=list[j]
			list[j]=temp
	return list
print(even_odd(list))