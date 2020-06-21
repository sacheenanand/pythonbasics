# to count the words in string, just count how many words are in the sentence.
str = "my name123 is hero and I am not1 joking"
string = "to count the words in string, just count how many words are in the sentence."


def count_words(str):

	if len(str.split())==0:
		return None

	number_words = 0
	prev_char = None

	for ch in str.split():
		cur_char = ch.isalpha()
		print(cur_char)
		

		if not prev_char and cur_char:

			number_words+=1
		else:
			prev_char = cur_char
			
	return number_words
print(count_words(str))