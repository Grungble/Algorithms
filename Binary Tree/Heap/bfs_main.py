from h_node import Node
tree_list = []
def __add__(root:Node, new_value:int):
    root_value = root.value
    if new_value == root_value:
        print("hello")


if __name__ == '__main__':
    root_node = Node(10,0)
    __add__(root_node)
    print("hello")