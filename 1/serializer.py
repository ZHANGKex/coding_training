class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.children = []

    def add_children(self, child):
        self.add_children.append(child)

import json

def serialize_to_json(node, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return {'id': node.id}
    
    visited.add(node)

    serialized_node = {
        "id": node.id,
        "value": node.value,
        "children": []
    }

    for child in node.children:
        serialized_node["children"].append(serialize_to_json(child, visited))

    return serialized_node

if __name__ == "__main__":
    root = Node(1, "Root")
    child1 = Node(2, "child 1")
    child2 = Node(3, "Child 2")