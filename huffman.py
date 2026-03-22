class Node:
    """
    Node class for Huffman Tree
    """
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def calculate_frequency(text):
    frequency = {}
    
    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    
    return frequency


def find_min_node(nodes):
    min_index = 0
    
    for i in range(1, len(nodes)):
        if nodes[i].freq < nodes[min_index].freq:
            min_index = i
    
    return nodes.pop(min_index)


def build_huffman_tree(frequency):
    nodes = []
    
    for ch in frequency:
        nodes.append(Node(ch, frequency[ch]))
    
    while len(nodes) > 1:
        left = find_min_node(nodes)
        right = find_min_node(nodes)
        
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        
        nodes.append(parent)
    
    return nodes[0]


def generate_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    
    if root.char is not None:
        if current_code == "":
            codes[root.char] = "0"
        else:
            codes[root.char] = current_code
        return codes
    
    if root.left is not None:
        generate_codes(root.left, current_code + "0", codes)
    
    if root.right is not None:
        generate_codes(root.right, current_code + "1", codes)
    
    return codes


def encode(text, codes):
    encoded_text = ""
    
    for ch in text:
        encoded_text += codes[ch]
    
    return encoded_text


def decode(encoded_text, root):
    decoded_text = ""
    current = root
    
    for bit in encoded_text:
        if bit == "0":
            current = current.left
        else:
            current = current.right
        
        if current.char is not None:
            decoded_text += current.char
            current = root
    
    return decoded_text

    
    # YOUR CODE HERE
    
    return decoded_text


def huffman_compression(text):
    """
    Main function - DO NOT MODIFY
    This will test your implementation
    """
    print("Original text: " + text)
    print("Original size: " + str(len(text) * 8) + " bits")
    print()
    
    # Step 1: Calculate frequencies
    frequency = calculate_frequency(text)
    print("Character frequencies: " + str(frequency))
    print()
    
    # Step 2: Build Huffman tree
    root = build_huffman_tree(frequency)
    print("Huffman tree built")
    print()
    
    # Step 3: Generate codes
    codes = generate_codes(root)
    print("Huffman codes: " + str(codes))
    print()
    
    # Step 4: Encode
    encoded = encode(text, codes)
    print("Encoded: " + encoded)
    print("Encoded size: " + str(len(encoded)) + " bits")
    print()
    
    # Step 5: Decode
    decoded = decode(encoded, root)
    print("Decoded: " + decoded)
    print("Success: " + str(decoded == text))
    print()
    
    if len(encoded) > 0:
        compression_ratio = (1 - len(encoded) / (len(text) * 8)) * 100
        print("Compression: " + str(round(compression_ratio, 2)) + "%")


# Test your implementation
if __name__ == "__main__":
    # Start with simple test
    test_text = "aabbc"
    huffman_compression(test_text)
    
    print()
    print("=" * 50)
    print()
    
    # Try with longer text
    test_text2 = "huffman coding algorithm"
    huffman_compression(test_text2)