print("hello ")
list = []
while 1:
    ToDoinput = raw_input()
    if (ToDoinput =="exit"):
        break
    priority, name, date, state = ToDoinput.split()
    list.insert(int(priority),[int (priority) , name , date, state])
    pr = 1
    for item in list:
        print ("{} ) ToDo: {}   dead line: {} satatus: {} ".format(pr , list[pr-1][1], list[pr-1][2], list[pr-1][3]))
        pr+= 1
