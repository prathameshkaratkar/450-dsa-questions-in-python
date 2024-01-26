# reverse the array in python 

def reverseWord(s):
    l = list(s)
    l.reverse()
    return "".join(l)

s = 'hello'
sum = reverseWord(s)
print(sum)