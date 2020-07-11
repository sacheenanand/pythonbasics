def anagram(string1, string2):
	count = {}

	for i in string1:
		if i in count:
			count[i]+=1
		else:
			count[i]=1
	for i in string2:
		if i in count:
			count[i]-=1
		else:
			count[i]=1
	for k in count:
	#	print(k)
	#	print(count)
		if count[k]!=0:
			return False
	return True

print("here you go",anagram("silent","listen"))
print("here you go",anagram("dad","cad"))






