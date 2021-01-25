
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, val):
        self.val = val
        
    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head =  head
        self.count =  0

    def get_count(self):
        return self.count

    def insert(self, data):
        new_node = Node(data)

    def find(self, val):
        item = self.head

        return None

    def deleteAt(self, idx):
        if idx > self.count-1:
            return 

    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print ("Node:", tempnode.get_data())
            tempnode = tempnode.get_next()

def main():
    pass

if __name__ == "__main__":
    main()