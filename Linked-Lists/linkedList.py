class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head
    
    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, data):
        #creates a new temporary node that stores the data
        temp = Node(data)
        #sets the temp nodes next pointer to the head of the list
        temp.next = self.head
        #makes temp the head
        self.head = temp
        return self.head

    def insert_at_tail(self,data):
        if self.head is None:
            self.insert_at_head(data)

        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node(data)

   # def insert_at_K(self, data, k):


    def print_list(self):
        if self.head is None:
            print("Null list")
            return
        
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        print('None')

LL = LinkedList()
LL.print_list()
print('Inserting values into list')
for i in range(5):
    LL.insert_at_head(i)

LL.print_list()
LL.insert_at_tail(420)
LL.print_list()

