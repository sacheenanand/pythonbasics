#compress a string using run length encoding, so the string "aaabbbbcccbbb" becomes "a3b4c3b3"

def run_lenth_encoding(string):
	if not string:
		return string


	p =0
	result = []

	while p<len(string):
		c = string[p]

		count = 0

		while p < len(string) and c == string[p]:
			count+=1
			p+=1
	result.append(str(c))
	result.append(str(count))
	return ''.join(result)
print(run_lenth_encoding("aabbbbbccccc"))



