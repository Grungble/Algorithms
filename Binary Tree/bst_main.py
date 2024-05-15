from bst_node import Node

def insert(root:Node, new_name:str, new_value:int):
    root_value = root.value
    if root_value == new_value:
        #No operation
        print("value already there")
        return
    if new_value < root.value and root.left_node is None:
        print('inserting left')
        new_left_node = Node(new_name, new_value)
        root.left_node = new_left_node
        return
    if new_value > root.value and root.right_node is None:
        print('inserting right')
        new_right_node = Node(new_name, new_value)
        root.right_node = new_right_node
        return
    #Recurse
    next_root = None
    if new_value < root.value:
        print('going left')
        next_root = root.left
    else:
        print('going right')
        next_root = root.right
    insert(next_root, new_name, new_value)
def print_tree(root:Node):
    pass
if __name__ == '__main__':
    my_root_node = Node('Node root', 7)
    print(my_root_node)
    insert(my_root_node, 'Luffy',6)
    print_tree(my_root_node)