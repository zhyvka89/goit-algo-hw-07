class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

### ЗАВДАННЯ 1 ###
def max_val(root):
    if root is None:
      return None
    
    current = root
    while current.right is not None:
        current = current.right
    
    return current.val

### ЗАВДАННЯ 2 ###
def min_val(root):
    if root is None:
      return None
    
    current = root
    while current.left is not None:
        current = current.left
    
    return current.val

### ЗАВДАННЯ 3 ###
def sum_val(root):
    if root is None:
      return 0
    
    left_sum = sum_val(root.left)
    right_sum = sum_val(root.right)

    return root.val + left_sum + right_sum


# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 15)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

max_value = max_val(root)
print("Найбільше значення в дереві:", max_value)

min_value = min_val(root)
print("Найменше значення в дереві:", min_value)

sum_of_all_values = sum_val(root)
print("Сума усіх значень в дереві:", sum_of_all_values)