                                                                              #Assignment 21

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Questions 1 Ans
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def inorder_traversal(root, sorted_list, index):
    if root:
        inorder_traversal(root.left, sorted_list, index)
        root.val = sorted_list[index[0]]
        index[0] += 1
        inorder_traversal(root.right, sorted_list, index)

def convert_to_bst(root):
    # Step 1: Store node values in a list
    def store_values_in_list(root, values):
        if root:
            store_values_in_list(root.left, values)
            values.append(root.val)
            store_values_in_list(root.right, values)

    values = []
    store_values_in_list(root, values)

    # Step 2: Sort the list
    values.sort()

    # Step 3: Update node values in the binary tree
    index = [0]  # Using a mutable object to keep track of the index
    inorder_traversal(root, values, index)

    return root

# Example usage
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

converted_root = convert_to_bst(root)

# Output the resulting binary search tree using an inorder traversal
def inorder_print(root):
    if root:
        inorder_print(root.left)
        print(root.val, end=" ")
        inorder_print(root.right)

inorder_print(converted_root)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Questions 2 Ans
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def construct_bst(values):
    root = None
    for value in values:
        root = insert_node(root, value)
    return root

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_node(root.left, value)
    elif value > root.val:
        root.right = insert_node(root.right, value)
    return root

def find_lca(root, node1, node2):
    if root is None:
        return None
    if root.val > node1 and root.val > node2:
        return find_lca(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        return find_lca(root.right, node1, node2)
    return root

def find_distance(root, value):
    if root.val == value:
        return 0
    if value < root.val:
        return 1 + find_distance(root.left, value)
    return 1 + find_distance(root.right, value)

def distance_between_nodes(values, node1, node2):
    root = construct_bst(values)
    lca = find_lca(root, node1, node2)
    distance1 = find_distance(lca, node1)
    distance2 = find_distance(lca, node2)
    return distance1 + distance2

# Example usage
values = [8, 3, 1, 6, 4, 7, 10, 14, 13]
node1 = 6
node2 = 14

distance = distance_between_nodes(values, node1, node2)
print("The distance between the two keys:", distance)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------

#Questions 3 Ans

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class DoublyLinkedListNode:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

def binary_tree_to_doubly_linked_list(root):
    if root is None:
        return None

    # Helper function to perform inorder traversal
    def inorder(node):
        nonlocal prev
        nonlocal head

        if node is None:
            return

        inorder(node.left)

        # Convert current node to doubly linked list node
        current = DoublyLinkedListNode(node.val)
        if prev is None:
            head = current
        else:
            prev.next = current
            current.prev = prev
        prev = current

        inorder(node.right)

    prev = None
    head = None

    # Perform inorder traversal to convert binary tree to doubly linked list
    inorder(root)

    return head

# Helper function to print the doubly linked list
def print_doubly_linked_list(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Example usage
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(30)
root.right.right = TreeNode(35)

# Convert binary tree to doubly linked list
doubly_linked_list_head = binary_tree_to_doubly_linked_list(root)

# Print the doubly linked list
print_doubly_linked_list(doubly_linked_list_head)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------


#Questions 4 Ans
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

def connect_nodes_at_same_level(root):
    if root is None:
        return None

    # Perform level-order traversal
    queue = [root]

    while queue:
        level_size = len(queue)

        # Connect nodes at the current level
        for i in range(level_size):
            node = queue.pop(0)

            if i < level_size - 1:
                node.next = queue[0]
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return root

# Helper function to print the connections at each level
def print_connections_at_each_level(root):
    current = root
    while current:
        level_start = current
        while current:
            print(current.val, end=" → ")
            current = current.next
        print("-1")
        current = level_start.left

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Connect nodes at the same level
connect_nodes_at_same_level(root)

# Print the connections at each level
print_connections_at_each_level(root)


