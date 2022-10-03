class DoubleNode:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, key, value):
        # checking if head is None
        if self.head is None:
            # creating head with provided key and value
            self.head = DoubleNode(key, value)
            self.tail = self.head
            return 
        
        # if head is not none then adding it to the tail
        # new node is always added to tail
        self.tail.next = DoubleNode(key, value)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    
    def remove(self,node):
        # checking if node value or key are none
        if node.value is None or node.key is None:
            return None

        # Checking if the node is head
        if self.head == node:
            # moving head to the next element 
            self.head = self.head.next
            self.head.previous = None
            # returning key to remove it from dict
            return node.key

        # if node is not the head and is in between the linked list removing that node from the linked list
        node.previous.next = node.next
        node.next.previous = node.previous
        #  returning key for that node to remove from dict
        return node.key
        #[4,5,3]

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        # self.cache stores node as a value with the provided key
        self.cache = {}
        self.capacity = capacity
        # Creating the linked list
        self.linked_list = LinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        # check key in the dict of self.cache
        if key in self.cache:
            #take the value which will be node of linkedlist for that specific key 
            node = self.cache[key]

            # Remove that node from the linked list 
            self.linked_list.remove(node)

            # Insert again the same node using append that will insert at the tail
            self.linked_list.append(node.key, node.value)

            # return the node value for that specific key
            return node.value
        
        # If key is not present in the dict then return -1
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # Checking the len of the dict if its less then capacity
        if len(self.cache)<self.capacity:

            # Appending the value into linked list which will be append at the tail of the linked list
            self.linked_list.append(key, value) 

            # Adding the linked list tail into the dict for that key
            self.cache[key]=self.linked_list.tail
        else:
            # removing the least used in our case it will be always head node and key for that node is returned to remove it from the cache
            k = self.linked_list.remove(self.linked_list.head)

            # Data for that specific key removed from the cache
            self.cache.pop(k)

            # Added new key and value into the linked list
            self.linked_list.append(key, value) 

            #Added new tail of the linked list for that specific key into cache 
            self.cache[key]=self.linked_list.tail
            
# printing dictionary with linkedlist as value
def print_dict(dict_data):
    for k, v in dict_data.items():
        print(k, ":", v.value)
our_cache = LRU_Cache(5)

# printing linked list
def print_Linkedlist(node):
    while node is not None:
        print('link: ',node.value)
        node = node.next

# # Add your own test cases: include at least three test cases
# # and two of them must include edge cases, such as null, empty or very large values
#Test Case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# # Test Case 2
test_2_cache = LRU_Cache(2)
print(test_2_cache.get(500000)) #return -1

# # Test Case 3
our_cache.set(36,55) # removes 4 and sets 55, since 4 was least used entry

