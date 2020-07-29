# example ,string = "my name is sacheen" should be "sacheen is name my"

def rev_word(string):
    s = string.split(" ")
    head = 0
    tail = len(s)-1
    while head < tail:
        temp = s[tail]
        s[tail]= s[head]
        s[head]= temp
        head+=1
        tail-=1
    return s
print("here you go",rev_word("my name is sacheen"))
print("here you go",rev_word("I live in walnutcreek"))