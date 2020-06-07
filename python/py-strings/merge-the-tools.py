from collections import OrderedDict 

def merge_the_tools(string, k):
    l=list(string[0+i:k+i] for i in range(0, len(string), k))
    for i in l: print("".join(OrderedDict.fromkeys(i)))

