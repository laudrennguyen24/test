class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def count_elements(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def add_at_position(self, data, position):
        if position == 0:
            self.add_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        if not current:
            return
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if not self.head:
            return
        self.head = self.head.next

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next
        if not current or not current.next:
            return
        current.next = current.next.next

    def delete_all_values(self, value):
        while self.head and self.head.data == value:
            self.head = self.head.next
        current = self.head
        while current and current.next:
            if current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

    def update_values(self, old_value, new_value):
        current = self.head
        while current:
            if current.data > old_value:
                current.data *= 5
            current = current.next

    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def find_min(self):
        if not self.head:
            return None
        min_value = self.head.data
        current = self.head.next
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next
        return min_value

    def find_max(self):
        if not self.head:
            return None
        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

# Ví dụ sử dụng
linked_list = LinkedList()
linked_list.add_at_beginning(1)
linked_list.add_at_end(10)
linked_list.add_at_end(14)
linked_list.add_at_end(7)

linked_list.print_list()  # In ra toàn bộ danh sách
print("Số phần tử:", linked_list.count_elements())  # Đếm số phần tử

linked_list.add_at_position(5, 2)  # Thêm số 5 vào vị trí thứ 2
linked_list.print_list()

linked_list.delete_at_beginning()  # Xoá đầu
linked_list.delete_at_end()  # Xoá cuối
linked_list.delete_at_position(1)  # Xoá vị trí thứ 1
linked_list.print_list()

linked_list.delete_all_values(10)  # Xoá tất cả số 10
linked_list.print_list()

linked_list.update_values(10, 5)  # Tìm và tăng các số >10 lên gấp 5 lần
linked_list.print_list()

print("Tìm min:", linked_list.find_min())  # Tìm min
print("Tìm max:", linked_list.find_max())  # Tìm max

linked_list.reverse()  # Đảo chiều danh sách
linked_list.print_list()