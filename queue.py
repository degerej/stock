from linkedlist import LinkedList


class Queue:
    def __init__(self):
        self.my_list = LinkedList()

    def push(self, data):
        self.my_list.add_end(data)

    def pop(self):
        return self.my_list.remove_head()
