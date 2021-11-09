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

    def insert_at_K(self, data, k):
        if k < 0:
            print('Invalid position')
        
        #Case 1: K = 0 -> insert at head
        if k == 0:
            self.insert_at_head(data)
            return
        
        count = 0
        ptr = self.head

        while ptr:
            if count == k-1:
                break
            ptr = ptr.next
            count += 1
        
        if count <= k-1 and not ptr:
            print('Index out of bounds')
            return
        # Case 2: Insert somewhere in the middle of the list
        if count == k-1 and ptr.next:
            new_node = Node(data)
            new_node.next = ptr.next
            ptr.next = new_node
        # Case 3: Insert Node at the tail
        else:
            self.insert_at_tail(data)

    def delete_head(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.head.next
        temp = None
    
    def delete(self, data):
        if self.is_empty():
            return False
        if self.head.data == data:
            self.delete_head()
            return True

        ptr = self.head
        prev = None

        while ptr:
            if ptr.data == data:
                prev.next = ptr.next
                return True
            prev = ptr
            ptr = ptr.next
        return False

    def search(self, data):
        if not self.head:
            return False
        
        ptr = self.head
        while ptr:
            if ptr.data == data:
                return True
            ptr = ptr.next
        return False
    
    def search_recursion(self, head, data):
        if not head:
            return False

        if head.data == data:
            return True
        
        return self.search_recursion(head.next, data)


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
for i in range(5):
    LL.insert_at_head(i)

LL.print_list()
LL.delete(0)
LL.print_list()
print(LL.search_recursion(LL.head, 0))





