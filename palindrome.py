
def palindrome(string):
	head, tail =0, len(string)-1

	while head < tail:
		while not string[head].isalnum():
			head+=1
		while not string[tail].isalnum():
			tail-=1
		if string[head].lower()!=string[tail].lower():
			return False


		head+=1
		tail-=1

		return True
print("Is This Palindrome", palindrome("daaad"))
print("Is This Palindrome", palindrome("dance"))
print("Is This Palindrome", palindrome("dad dad"))
print("Is This Palindrome", palindrome("Eva, Can I Stab Bats In A Cave"))