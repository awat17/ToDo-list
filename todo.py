print("hello ")
list = []
i ,tmp = str(raw_input()).split()
list.insert(int(i),tmp)
i = 1
for item in list:
    print ("%d   %s " % (i , list[i-1]))
    i = i+1
