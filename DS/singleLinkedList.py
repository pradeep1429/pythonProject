class node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def traversal(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_begin(self, data):
        newNode = node(data)
        newNode.ref = self.head
        self.head = newNode
    def add_end(self,data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = newNode
    def get_node_pos(self, nodeData):
        n = self.head
        while n is not None:
            if n.data == nodeData:
                break
            n = n.ref
        return n
    def add_after_node(self,existingNodeData,data):
        n = self.get_node_pos(existingNodeData)
        if n is not None:
            newNode = node(data)
            newNode.ref = n.ref
            n.ref = newNode
        else:
            print("given node {} not present in list".format(existingNodeData))

    def add_before_node(self,existingNodeData,data):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.data == existingNodeData:
            self.add_begin(data)
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == existingNodeData:
                    break
                n = n.ref
            if n is not None:
                newNode = node(data)
                newNode.ref = n.ref
                n.ref = newNode
            else:
                print("given node {} not present in list".format(existingNodeData))


ll1 = linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_end(40)
ll1.add_after_node(60,50)
ll1.add_after_node(20,50)
ll1.add_before_node(20,70)

ll1.traversal()

