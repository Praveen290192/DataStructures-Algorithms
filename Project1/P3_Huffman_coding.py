import sys
# Creating a tree structure
class NodeTree:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def nodes(self):
        return (self.left, self.right)

# Generating the Huffman code for each character using recursion
def huffman_tree(node, code=''):
    if type(node) is str:
        return {node: code}
    (left_node, right_node) = node.nodes()
    output = {}
    output.update(huffman_tree(left_node, code + '0'))
    output.update(huffman_tree(right_node, code + '1'))
    return output

# Huffman encoding function
def huffman_encoding(data):

    # Getting the frequency of each Char
    freq = {}
    for char in data:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # Sorting it in Ascending order
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=False)

    # Merging node with minimum frequency to create Huffman tree 
    tree = freq
    while len(tree) > 1:
        (key1, v1) = tree[0]
        (key2, v2) = tree[1]
        tree = tree[2:]
        node = NodeTree(key1, key2)
        tree.append((node, v1 + v2))
        tree = sorted(tree, key=lambda x: x[1], reverse=False)

    # Huffman code for each Char in the input data in dict form
    encoded_data_dict = huffman_tree(tree[0][0])
    # Huffman code for input data
    encoded_data = ''
    for char in data:
        encoded_data +=encoded_data_dict[char]
    return encoded_data, tree

def huffman_decoding(data,tree):
    # Setting current node to root node
    current = tree[0][0]
    result = ''
    # looping over each char of huffman encoded data
    for char in data:
        if char == "0":
            current = current.left
        else:
            current = current.right
        # Resetting current node to root and appending Char
        if type(current) is str:
            result+=current
            current=tree[0][0]
    return result

def testing_loop(data):
    if data is None: 
        return "No data provided"

    print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    encoded_data, tree = huffman_encoding(data)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

if __name__ == "__main__":
    # Testing conditions
    codes = ["The bird is the word", "AAAAAAAABBBBBBBCCCCCDDEEEEFFFF",None,"this thing is new for me", "leaf eats sun light, deer eats leaf, tiger eats deer and death eats tiger"]
    
    testing_loop(codes[0])
    # Add your own test cases: include at least three test cases
    # and two of them must include edge cases, such as null, empty or very large values

    # Test Case 1
    testing_loop(codes[1])

    # Test Case 2
    testing_loop(codes[2])

    # Test Case 3
    testing_loop(codes[3])

    # Test Case 4
    testing_loop(codes[4])
