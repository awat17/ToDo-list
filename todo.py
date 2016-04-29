print("hello ")
list = []
class ToDo:
    ToDoCount = 0

    def __init__(self, priority, name, date, state):
        self.priority = priority
        self.name = name
        self.date = date
        self.state = state
        ToDo.ToDoCount +=1

    def new_item (self, priority, name, date, state):
            self.insert(int (self.priority), self.name, self.date, self.state )

    def count (self):
        print "all ToDo is %d" %ToDo.ToDoCount

    def displayToDo(self):
      print "Name : ", self.name,  ", date: ", self.date
pr = 1
while 1:
    priority, name, date, state = raw_input().split()
    list.insert(int(priority),ToDo(priority, name, date, state))
    for item in list:
        print ("%d   %s " % (pr , list[pr-1]))
        pr = pr +1
