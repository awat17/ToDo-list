list = []
while(1):
    taskinput = str(raw_input())
    if( taskinput== "exit"):
        break
    i ,tmp , date = taskinput.split()
    list.insert(int(i), [tmp , date])
    pr = 1
    for item in list:
        print ("%d   %s " % (pr , list[pr-1]))
        pr = pr +1
