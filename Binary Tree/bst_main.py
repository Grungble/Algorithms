from bst_node import Node
list_tr = [3,5,10,2,6,16,8]
to_visit_queue = []
visited_set = []
def insert(root:Node, new_name:str, new_value:int):
    root_value = root.value
    if root_value == new_value:
        #No operation
        print("value already there")
        return
    if new_value < root.value and root.left_node is None:
        print('inserting', new_name,'left',new_value)
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
        next_root = root.left_node
    else:
        print('going right')
        next_root = root.right_node
    insert(next_root, new_name, new_value)
def print_tree(root:Node):
    pass
if __name__ == '__main__':
    my_root_node = Node('Node root', 7)
    for en, i in enumerate(list_tr):
        insert(my_root_node,f'node{en}',i)
        print_tree
    while len(to_visit_queue)>0:
        visited_set.append(to_visit_queue.pop(0))
    print_tree(my_root_node)