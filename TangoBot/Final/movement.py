
class Node:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)

n1.connected_to = {n2}
n2.connected_to = {n1, n3, n7}
n3.connectged_to = {n2, n8}
n6.connected_to = {n11, n7}
n7.connected_to = {n2, n6, n12}
n8.connected_to = {n3}
n11.connected_to = {n6}
n12.connected_to = {n7, n13}
n13.connected_to = {n12}
