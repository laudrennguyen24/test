class Phone:
    ID = None
    name = None
    price = 0
    color = None

    def __init__(self, ID, name, p, c):
        self.ID = ID
        self.name = name
        self.price = p
        self.color = c

    def printPhone(self):
        # print all infomation of a Phone object
        # begin your code here
        print('ID', self.ID)
        print('Name', self.name)
        print('price', self.price)
        print('color', self.color)
        # end your code here


class Node:
    info = None
    p_next = None

    def __init__(self, val):
        self.info = val


class Queue:
    head = None
    tail = None

    def __init__(self, node=None):
        # begin your code here
        self.head = node
        self.tail = node
        # end your code here

    def show(self):
        # begin your code here
        current = self.head
        while current is not None:
            current.info.printPhone()
            current = current.p_next
        # end your code here

    def enqueue(self, node):
        # begin your code here
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.p_next = node
            self.tail = node
        # end your code here
        
    def dequeue(self):
        # begin your code here
        if self.head is None:
            return None
        else:
            removed_node = self.head
            self.head = self.head.p_next
            if self.head is None:
                self.tail = None
            return removed_node
        # end your code here

    def is_empty(self):
        # begin your code here\
        return self.head is None
        # end your code here

    def count(self):
        # begin your code here
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.p_next
        return count
        # end your code here
    
    def front(self):
        # get the head's info
        # begin your code here
        if self.head is not None:
            return self.head.info
        return None
        # end your code here

    def get3(self):
        # get the first three elements, print them to the screen,
        # then remove them out of the queue
        # begin your code here
        current = self.head
        count = 0
        while current is not None and count < 3:
            current.info.printPhone()
            current = current.p_next
            count += 1
        while count > 0:
            self.dequeue()
            count -= 1
        # end your code here
    
    def reverse(self):
        # begin your code here
        prev = None
        current = self.head
        while current is not None:
            next_node = current.p_next
            current.p_next = prev
            prev = current
            current = next_node
        self.tail = self.head
        self.head = prev
        # end your code here

    def sortQueue(queue):
        if queue.is_empty():
            return

        # Get all elements from the queue
        elements = []
        while not queue.is_empty():
            node = queue.dequeue()
            elements.append(node.info)

        # Sort the elements based on a specific attribute (e.g., ID)
        sorted_elements = sorted(elements, key=lambda phone: phone.ID)

        # Enqueue the sorted elements back into the queue
        for phone in sorted_elements:
            queue.enqueue(Node(phone))


if __name__ == "__main__":

    p = Phone(12,'Iphone pro max', 1000, 'black')
    n = Node(p)
    myqueue = Queue(n)

    # write some test cases for your functions
    # begin your code here
    myqueue.show()
    p2 = Phone(15, 'Samsung Galaxy', 900, 'white')
    n2 = Node(p2)
    myqueue.enqueue(n2)
    myqueue.show()
    dequeued_node = myqueue.dequeue()
    if dequeued_node:
        print('Dequeued Node:')
        dequeued_node.info.printPhone()
    print('Is Empty:', myqueue.is_empty())
    print('Count:', myqueue.count())
    front_node = myqueue.front()
    if front_node:
        print('Front Node:')
        front_node.printPhone()
    myqueue.get3()
    myqueue.reverse()
    myqueue.show()
    myqueue = Queue()
    # Enqueue some elements into the queue
    myqueue.sortQueue()
    # Display the sorted queue
    myqueue.show()

    # end your code here
