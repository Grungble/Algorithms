
class Node:
    def __init__(self,value:int,row:int):
        self.value = value
        self.row = row

    def __repr__(self):
        repr_str = f'Tree(name={self.name},value={self.value})'
        return repr_str
    def __str__(self):
        return self.__repr__()
