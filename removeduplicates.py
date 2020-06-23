# python to code remove duplicates letters ib a string

string = "hheelllloo"

def remove_duplicates(string):
	empty_string = ""
	for i in string:
		if i not in empty_string:
			empty_string += i
		else:
			pass
	return empty_string
print(remove_duplicates("hheelllloo"))