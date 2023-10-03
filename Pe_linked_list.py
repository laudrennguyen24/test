#Thai Hoc
class StudentNode:
    def __init__(self,id,name,address,score,next=None):
        self.id = id
        self.name = name
        self.address = address
        self.score = score
        self.next = next
class Student_list:
    def __init__(self):
        self.head = None

    def add_student(self,id,name,address,score):
        new_node = StudentNode(id, name, address, score)
        if self.head == None:
            self.head = new_node
        else:
            tmp = self.head
            while tmp.next != None:
                if tmp.id == id:
                    print('Student id already exists!')
                    return
                tmp = tmp.next
            tmp.next = new_node
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.id,tmp.name,tmp.address,tmp.score,sep = ' ')
            tmp=tmp.next
    def delete_student(self,id):
        if self.head == None:
            print('The list of Student is empty')
            return
        else:
            if self.head.id == id:
                self.head = self.head.next
                print('Student deleted!')
                return
            else:
                tmp = self.head
                while tmp != None:
                    if tmp.next.id == id:
                        tmp.next = tmp.next.next
                        print('Student Deleted!')
                        return
                    tmp = tmp.next
                print ('Student ID not found!')

    def update_student(self,id,name,address,score):
        if self.head == None:
            print('The List is empty!')
            return
        else:
            tmp = self.head
            while tmp != None:
                if tmp.id == id:
                    tmp.name = name
                    tmp.address = address
                    tmp.score = score
                    print("Student information updated!")
                    return
                tmp = tmp.next
            print("Stduent ID not found!")
    def search_Student(self,id):
        if self.head == None:
            print('The list is empty!')
            return
        else:
            tmp = self.head
            while tmp != None:
                if tmp.id == id:
                    print(f'ID: {tmp.id} Name: {tmp.name} Address: {tmp.address} Score: {tmp.score}')
                    return
                tmp = tmp.next
            print ('Student ID not found')
    def search(self,id):
        if self.head == None:
            return False
        else:
            tmp = self.head
            while tmp:
                if tmp.id == id:
                    return True
                tmp = tmp.next
            return False
    def menu(self):
        print('Welcome to the student managemetn program!')
        print('Please choose one of the following options:')
        print('''1.Add a new student\n2. Update a student information\n3.Delete a student\n4.Search for student ID\n5.exit the program
        ''')
        while True:
            choice = input('Enter your choice:')
            if choice in ['1','2','3','4','5']:
                if choice == '1':
                    id = input('Enter student id: ')
                    name = input('Enter student name: ')
                    address = input('Enter the student address: ')
                    score = input("Enter the student's score: ")
                    self.add_student(id,name,address,score)
                elif choice == '2':
                    id = input('Enter student id: ')
                    name = input('Enter student name: ')
                    address = input('Enter the student address: ')
                    score = input("Enter the student's score: ")
                    self.update_student(id,name,address,score)
                elif choice == '3':
                    id = input('Enter the student ID: ')
                    self.search_Student(id)
                elif choice == '4':
                    id = input('Enter the student ID: ')
                    self.delete_student(id)
                else:
                    print('Goodbye!')
                    break
            else:
                print('Your choice is Invalid. Please choose number from 1 to 5.')
if __name__ =='__main__':
    students = Student_list()

    students.add_student("123", "Alice", "123 Main Street", "90")
    students.add_student("456", "Bob", "456 Park Avenue", "80")
    students.add_student("789", "Charlie", "789 Elm Street", "70")

    students.menu()
    students.print_list()
    print(students.search('123'))
    print(students.search('486'))
    print(students.search('789'))
    students.print_list()


