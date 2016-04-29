print("hello ")
list = []
pr = 1
while 1:
    ToDoinput = raw_input()
    if (ToDoinput =="exit"):
        break
    priority, name, date, state = ToDoinput.split()
    list.insert(int(priority),[int (priority) , name , date, state])
    for item in list:
        print ("{} ) ToDo: {}   dead line: {} satatus: {} ".format(pr , list[pr-1][1], list[pr-1][2], list[pr-1][3]))
        pr+= 1
