import hashlib
from datetime import datetime
import time

class Block:

    def __init__(self, timestamp, data, previous_hash, previous_node):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_node = previous_node
        self.hash = self.calc_hash(timestamp)

    def calc_hash(self,timestamp):
        sha = hashlib.sha256()

        hash_str = str(timestamp).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp,data,0, None)
            self.tail = Block(timestamp,data,0, None)
            return
        pre_hash = self.tail.hash
        pre_node = self.tail
        self.tail = Block(timestamp,data, pre_hash, pre_node)
        return
    
    def PrintLinkedList(self):
        node = self.tail
        while node is not None:
            print(node.timestamp, node.data, node.hash, node.previous_hash)
            node = node.previous_node
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
LL = LinkedList()
# Test Case 1
LL.append(datetime.now(), "test1")
time.sleep(1)
# Test Case 2
LL.append(datetime.now(), "test2")
time.sleep(1)
# Test Case 3
LL.append(datetime.now(), "test3")
LL.PrintLinkedList()
