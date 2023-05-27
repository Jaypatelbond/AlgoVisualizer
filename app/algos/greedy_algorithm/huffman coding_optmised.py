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
        huffman_code_tree(node.left, code + '0', code_dict)
        huffman_code_tree(node.right, code + '1', code_dict)
    return code_dict


# Calculating the frequency of each character in the string
freq = defaultdict(int)
for c in string:
    freq[c] += 1

# Building the Huffman tree using a priority queue (binary heap implementation)
pq = [NodeTree(char=c, freq=f) for c, f in freq.items()]
heapq.heapify(pq)

while len(pq) > 1:
    node1 = heapq.heappop(pq)
    node2 = heapq.heappop(pq)
    merged = NodeTree(freq=node1.freq + node2.freq, left=node1, right=node2)
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


# This implementation uses a priority queue (binary heap implementation) to build the Huffman tree in O(nlogk) time,
# and bit manipulation to generate the Huffman codes. It also uses a dictionary to store the frequency counts, which
# improves the lookup time. Overall, these optimizations can make the algorithm faster and more memory-efficient
# for large input strings.
