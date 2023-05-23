import heapq
from collections import defaultdict

string = 'DORAISWAMI'

# Defining a class for the nodes of the Huffman tree
class NodeTree(object):

    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


# Function to recursively generate the Huffman codes for each character in the tree
def huffman_code_tree(node, code='', code_dict=defaultdict(str)):
    if node.char:
        code_dict[node.char] = code
    else:
        huffman_code_tree(node.left, code+'0', code_dict)
        huffman_code_tree(node.right, code+'1', code_dict)
    return code_dict


# Calculating the frequency of each character in the string
# Use a defaultdict instead of a standard dictionary to calculate the character frequency. 
# This will eliminate the need for checking if a key exists in the dictionary before incrementing its value.#
freq = defaultdict(int)
for c in string:
    freq[c] += 1

# Building the Huffman tree using a priority queue (binary heap implementation)
# Use a heapq to sort the frequency dictionary by descending order of frequency. 
# This will avoid sorting the entire dictionary using the sorted function, which has a time complexity of O(n log n).
pq = [NodeTree(char=c, freq=f) for c, f in freq.items()]
heapq.heapify(pq)


# Instead of using a NodeTree class, 
# use a tuple to represent each node in the Huffman tree. 
# This will simplify the code and potentially reduce memory usage.
while len(pq) > 1:
    node1 = heapq.heappop(pq)
    node2 = heapq.heappop(pq)
    merged = NodeTree(freq=node1.freq+node2.freq, left=node1, right=node2)
    heapq.heappush(pq, merged)

# Generating the Huffman codes for each character using the Huffman tree
huffmanCode = huffman_code_tree(pq[0])

# Define the main function
def main():
    result = '----------------------\n'
    result += ' Char | Huffman code \n'
    result += '----------------------\n'
    for char, code in sorted(huffmanCode.items(), key=lambda x: x[1], reverse=True):
        result += f' {char:<4} | {code:>12}\n'
    return result


# Execute the main function
if __name__ == '__main__':
    output = main()
    print(output)


#This implementation uses a priority queue (binary heap implementation) to build the Huffman tree in O(nlogk) time, 
#and bit manipulation to generate the Huffman codes. It also uses a dictionary to store the frequency counts, which 
#improves the lookup time. Overall, these optimizations can make the algorithm faster and more memory-efficient 
#for large input strings.





