class Phone:
    ID = None
    name = None
    price = 0
    color = None

    def __init__(self, ID, name, p, c):
        # begin your code here
        self.ID = ID
        self.name = name
        self.price = p
        self.color = c
        # end your code here

    
    def printPhone(self):
        # print all infomation of a Phone object
        # begin your code here
        print(f'ID: {self.ID}')
        print(f'name: {self.name}')
        print(f'price: {self.price}')
        print(f'color: {self.color}')
        # end your code here
        
        
class Node:
    info = None
    p_next = None

    def __init__(self, val):
        # begin your code here
        self.info = val
        self.p_next = None
        # end your code here


class Stack:
    head = None
    def __init__(self, node=None):
        # begin your code here
        self.head = node
        # end your code here
    
    def show(self):
        # print all Phone in the stack 
        # begin your code here
        current = self.head
        while current:
            current.info.printPhone()
            current = current.p_next
        # end your code here

    def push(self, phone):
        # begin your code here
        new_node = Node(phone)
        new_node.p_next = self.head
        self.head = new_node
        # end your code here
        
    def pop(self):
        # begin your code here
        if self.is_Empty():
            print('empty stack')
        popped = self.head
        self.head = self.head.p_next
        return popped.info
        # end your code here

    def is_Empty(self):
        # begin your code here
        return self.head is None
        # end your code here
    
    def front(self):
        # get the head's info
        # begin your code here
        if self.head:
            return self.head.info
        return None
        # end your code here
    
    def reverse(self):
        # begin your code here
        prev = None
        current = self.head
        while current:
            next_node = current.p_next
            current.p_next = prev
            prev = current
            current = next_node
        self.head = prev

        # end your code here

    def popUntil(self, name):
        # keep doing pop function until an Iphone is in the top of stack
        # begin your code here
        if self.is_Empty():
            print('empty stack!!')
        else:
            while self.head.p_next:
                if self.head.info.name == name:
                    break
                self.pop()
        # end your code here
        
    def cmd(self):
        p = Phone(102,'Iphone pro max', 1000, 'black')
        c = 'dai**hoc*fpt**'
        # with each character tmp in c, if tmp!=* then push the phone p into stack
        # and then create a new Phone p with new ID = old ID +1
        # if tmp=* then do the pop function
        # begin your code here
        for tmp in c:
            if tmp != '*':
                self.push(p)
                p = (p.ID +1, p.name, p.price , p.color)
            else:
                self.pop()
        # end your code here

if __name__ == "__main__":
    
    p = Phone(12,'Iphone pro max', 1000, 'black')
    n = Node(p)
    myStack = Stack(n)
    
    
    # write some test cases for your functions
    # begin your code here
    # Pushing phones into the stack
    myStack.push(Phone(12, 'iPhone 11', '800', 'Black'))
    myStack.push(Phone(13, 'iPhone 12', '1000', 'White'))
    myStack.push(Phone(15, 'Samsung Galaxy S20', '900', 'Blue'))
    myStack.push(Phone(14, 'Google Pixel 4', '700', 'Black'))

    # Display all elements in the stack
    print("Initial stack:")
    myStack.show()
    print('-----------------------------------------------------')
    # Pop the top element and display the updated stack
    popped_phone = myStack.pop()
    print("Popped phone:", popped_phone.printPhone())
    print('------------------------------------------------------')
    print("Stack after popping:")
    myStack.show()
    print('------------------------------------------------------')

    # Get the top element without removing it
    top_phone = myStack.front()
    if top_phone is not None:
        print("Top phone:", top_phone.printPhone())
    else:
        print("Stack is empty.")
    print('-----------------------------------------------------')
    # Reverse the stack and display the elements
    print("Reversed stack:")
    myStack.reverse()
    myStack.show()
    print('------------------------------------------------------')

    # Pop elements until a specific phone name is found
    name_to_find = 'iPhone 12'
    myStack.popUntil(name_to_find)
    print(f"Stack after popping until '{name_to_find}':")
    myStack.show()

    print('---------------finished---------------------------------')
    # end your code here
