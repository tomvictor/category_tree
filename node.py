class Node:
    def __init__(self, name, depth, instance):
        self.name = name
        self.depth = depth
        self.instance = instance
        self._children = list()

    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

    def has_children(self):
        return len(self._children)

    def to_dict(self):
        data = {
            "name": str(self.instance),
            "children": [node.to_dict() for node in self._children],
        }
        return data
