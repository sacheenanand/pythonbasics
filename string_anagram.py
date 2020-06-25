# to check if two string is Anagram or not

def string_anagram(s1,s2):
	s1 = s1.replace("", " ").lower()
	s2 = s2.replace("", " ").lower()

	count = {}

	for i in s1:
		if i in count:
			count[i] =1
		else:
			count[i]+=1
	for i in s2:
		if i in count:
			count[i]-=1
		else:
			count[i]=1
	for j in count:
		if count[j]!=0:
			return False
	return True
print("hello", string_anagram("silent", "listen"))





