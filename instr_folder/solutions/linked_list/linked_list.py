##################  Answer taken from student in Closers Dec 2015 cohort

###### Create the Node Class
###### Every Node has two variables
###### The next instance variable represents our "Pointer"
###### Default value of next instance variable is "None"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:

###### Initialize this with a self.head instance variable
###### This is really important because we will be reassigning the values to this instance variable throughout this entire class. 
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def print_backwards(self, node = None):
        if node == None:
            node = self.head
        if node.next != None:
            self.print_backwards(node.next)
        print(node.data)

###### The Node class is instantiated here
###### what is passed in as the "data" argument when insert is called is what will also be passed into the Node instance as the instance variable
###### More instance variables and local variables are made in here
###### self.head / node / new_node / prevnode and the like. remember we are just assigned values to variables here. we are not invoking methods
    def insert(self, data, index):
        new_node = Node(data)
        count = 1
        node = self.head
        if self.head == None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            while count <= index:
                prevnode = node
                if node.next == None and count != index:
                    print("Index out of range")
                    return False
                node = node.next
                count += 1
            prevnode.next = new_node
            new_node.next = node
            return True

###### create another node local variable here
###### Remember these "node" variables are LOCAL so they will not and SHOULD NOT be overlapping with others
    def search(self, data):
        count = 0
        node = self.head
        while node != None:
            if node.data == data:
                print("Found value \"{}\" at index {}".format(data, count))
                break
            count += 1
            node = node.next
        if node == None:
            print("Could not find \"{}\" in the list.".format(data))

###### Recursion. Shit calling itself in itself
    def recursive_search(self, data, node = None):
        if node == None:
            node = self.head
        if node.data == data:
            return True
        if node.next == None:
            return False
        return self.recursive_search(data, node.next)
            


###### Instantiate the Linked List Class
linkedlist = Linked_List()

###### Invoke the methods inside of this class
linkedlist.insert("A",0)
linkedlist.insert("B",1)
linkedlist.insert("C",2)
linkedlist.insert("D",3)
linkedlist.insert("E",4)
linkedlist.insert("AAA",0)
linkedlist.print_list()
linkedlist.search("AAA")
linkedlist.search("asdfsad")
print("BACKWARDS:")
linkedlist.print_backwards()


assert(linkedlist.recursive_search("D") == True),"Search for D should return True"
assert(linkedlist.recursive_search("dsdfasdsa") == False),"Search for dsdfasdsa should return False"
