mylist = ["blue","red","yellow","green","white","green","black","green"]
Repeated_word = "green"
i = 0
while i < len(mylist):
    if mylist[i] == Repeated_word:
        mylist.remove(Repeated_word)
    else:
        i += 1
print(mylist)
