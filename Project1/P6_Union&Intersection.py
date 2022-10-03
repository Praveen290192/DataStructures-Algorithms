from re import L


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    # Creating output linked list
    output = LinkedList()

    # Checking for None Linked list
    if llist_1.head is None:
        return llist_2
    if llist_2.head is None:
        return llist_1
    # Looping over linked list and appending to output list 
    cur_head = llist_1.head
    while cur_head is not None:
        output.append(cur_head.value)
        cur_head = cur_head.next

    cur_head = llist_2.head
    while cur_head is not None:
        output.append(cur_head.value)
        cur_head = cur_head.next
    # returning output
    return output

def intersection(llist_1, llist_2):
    # Your Solution Here
    # Checking for None Linked list
    if llist_1.head is None or llist_2.head is None:
        return 

    list1 = []
    list2 = []
    # Creating output linked list
    output = LinkedList()

    # Taking Unique values from each linked list
    cur_head = llist_1.head
    while cur_head is not None:
        if cur_head.value not in list1:
            list1.append(cur_head.value)
        cur_head = cur_head.next

    cur_head = llist_2.head
    while cur_head is not None:
        if cur_head.value not in list2:
            list2.append(cur_head.value)
        cur_head = cur_head.next

    # Checking for any intersection
    for i in list1:
        if i in list2:
            output.append(i)
    # returning output
    if output.size() >0:
        return output
    return 


# # Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("case1: Union",union(linked_list_1,linked_list_2))
print ("case1: Inter",intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("case2: Union",union(linked_list_3,linked_list_4))
print ("case2: Inter",intersection(linked_list_3,linked_list_4))

# # Add your own test cases: include at least three test cases
# # and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

# print(len(linked_list_5) )

print ("case3: Union",union(linked_list_5,linked_list_6))
print ("case3: Inter",intersection(linked_list_5,linked_list_6))

# Test Case 2
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print ("case4 union",union(linked_list_7,linked_list_8))
print ("case4 inter",intersection(linked_list_7,linked_list_8))

# Test Case 3
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21, 55555555555398488888888889333]
element_2 = [5,32,7,9,1,1,11,64,1,55555555555398488888888889333]

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print ("case5",union(linked_list_9,linked_list_10))
print ("case5",intersection(linked_list_9,linked_list_10))
