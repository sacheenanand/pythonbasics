#find the common elements in this twoo array

list1= [1,2,3,4,5,6]
list2=[1,2,3,8,9,10]

def common_elelment(list1, list2):
	result=[]
	pos1 = 0
	pos2 = 0

	while pos1<len(list1) and pos2<(list2):
		if list1[pos1]==list2[pos2]:
			result.append(list1[pos1])

			pos1+=1
			pos2+=1
		elif list1[pos1]>list2[pos2]:
			pos2+=1
		else:
			pos1+=1
	return result
print("here is the coomon elements in the list",common_elelment(list1, list2))
