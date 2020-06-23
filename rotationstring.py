# Given two strings, find if one string can be formed by rotating the characters of the other.


def string_rotation(string1, string2):

	if len(string1) != len(string2):
		return False

	temp = string1 + string1

	if temp.count(string2)>0:
		return True
	else:
		return False

print("can this be rotated", string_rotation("pqr", "rpq"))
print("can this be rotated", string_rotation("sacheen", "eensach"))
print("can this be rotated", string_rotation("aaa", "bbb"))
print("can this be rotated", string_rotation("ABCD", "ACBD"))
print("can this be rotated", string_rotation("ABCDEFG", "ABCD"))
print("can this be rotated", string_rotation("ABCDEFG", "1111"))
print("can this be rotated", string_rotation("ABCDEFG", "asasasa"))
