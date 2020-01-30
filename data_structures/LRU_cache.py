class LinkNode:
    pre = None
    next = None
    key = None
    value = None
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

class LRUCache:
    size = None
    capacity = 0
    head = LinkNode()
    tail = LinkNode()

    def __init__(self, size):
        self.size = size
        self.head.next = self.tail
        self.tail.pre = self.head

    def search(self, key):
        running_node = self.head
        while(running_node.next is not None):
            if(running_node.key == key):
                return running_node
            running_node = running_node.next

    def move_to_top(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.head.next.pre = node
        node.next = self.head.next
        node.pre = self.head
        self.head.next = node

    def put(self, key, value):
        found = self.search(key)
        if found is None:
            found = LinkNode(key, value)
            found.next = self.head.next
            found.pre = self.head
            self.head.next.pre = found
            self.head.next = found

            self.capacity += 1
            if self.capacity > self.size:
                removed_node = self.tail.pre
                removed_node.pre.next = self.tail
                self.tail.pre = removed_node.pre
                removed_node = None
                self.capacity -= 1   
        else:
            found.value = value
            self.move_to_top(found)
                 

    def get(self, key):
        found = self.search(key) 
        if found is not None:
            self.move_to_top(found)
        return found.value if found is not None else None

    def getFullCache(self):
        ret = []
        node = self.head.next
        while(node.next is not None):
            ret.append((node.key, node.value))
            node = node.next
        return ret

c = LRUCache(5)
c.put("a", 1)
c.put("b", 2)
c.put("c", 3)
c.put("d", 4)
c.put("e", 5)
c.put("f", 6)
c.put("g", 7)
print(c.getFullCache())
print(c.get('c'))
print(c.getFullCache())
c.put("h", 8)
print(c.getFullCache())
print(c.get("f"))
print(c.getFullCache())

