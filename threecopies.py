#Here is the program to give three first three letters of a string and make it three copies

def three_char(string):
    count=0
    empty_string = ""
    for i in string:
        if i not in empty_string:
            empty_string += i
            count+=1
        if count>2:
            break
    return empty_string+empty_string+empty_string
print("here you go", three_char("JAVA")
)

