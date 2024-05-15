
class Node:
    def __init__(self,name:str,value:int):
        self.name = name
        self.value = value
        self.left_node = None
        self.right_node = None

    def __repr__(self):
        repr_str = f'Tree(name={self.name},value={self.value})'
        return repr_str
    def __str__(self):
        return self.__repr__()