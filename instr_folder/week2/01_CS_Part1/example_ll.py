import pudb

class Node:
    '''a nugget of data and a pointer'''
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, data):
        '''
        appends data to the end of a LL
        '''
        end = Node(data)
        n = self.head
        while n.next != None:
            n = n.next
        n.next = end

    def search(self, data):
        '''
        finds if data exists in a LL
        '''
        n = self.head
        while n != None:
            if n.data == data:
                return True
            else:
                n = n.next
        return False

    def delete(self, data):
        '''
        return LL at head position
        '''
        n = self.head
        # if head data is data, move head to head.next
        if (n.data == data):
            return n.next

        while n.next != None:
            if n.next == data:
                n.next = n.next.next
                return self
            n = n.next

        return self

    def print_ll(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next

    def insert(self, data, index):
        '''
        inserts data at index position
        '''
        n = self.head
        new = Node(data)
        counter = 0

        while n.next != None:
            if counter == index:
                new.next = n.next
                n.next = new
            n = n.next


def ll_builder(ll, list_of_data_to_add):
    pu.db
    for data in list_of_data_to_add:
        my_ll.append(data)
    return ll

# make a ll with 'A' head data
my_ll = LinkedList(Node('A'))

# add B - G data to ll
my_ll = ll_builder(my_ll, [chr(x) for x in range(66, 72)])

# print ll
my_ll.print_ll()

# should be True
print(my_ll.search('G'))

# should be False
print(my_ll.search('Y'))




