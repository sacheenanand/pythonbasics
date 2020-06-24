# Here is the program to check if parenthesis is valid or not, first create a dictionary and add all parenthesis to it as key and values, from the given string take all 

def part(s):
    dict = {'(':')', '[':']', '{':'}'}
    stack = []


    for i in s:
        if i in dict:
            stack.append(dict[i])
            print(stack)
            #print(dict)
        else:
            if len(stack)==0 or stack.pop()!=i:
                return False
    return True

print("is it True or False: ", part("{}"))
print("is it True or False: ", part("{)"))
print("is it True or False: ", part("{"))
print("is it True or False: ", part(")("))
print("is it True or False: ", part("{)"))
print("is it True or False: ", part("{[]}"))
print("is it True or False: ", part("{([])}"))