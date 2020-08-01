#list = [2,4,5,6,7,9]

def first_last(list):
    for i in range(0, len(list)-1):
        return(list[0], list[len(list)-1])
print("here you go", first_last([2,4,5,6,7,9]))
print("here you go", first_last([2,4,5,6,7,9,4,3]))
print("here you go", first_last([2,4,5,6,7,9,1,2,3,1]))
print("here you go", first_last([2,4,5,6,7,9,5,4,3,2,1]))