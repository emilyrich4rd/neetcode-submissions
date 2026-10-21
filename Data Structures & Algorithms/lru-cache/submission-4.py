class LRUCache:

    class Node:
        def __init__(self, prev=None, next=None, key=None, value=None):
            self.prev = prev
            self.next = next
            self.key = key
            self.value = value

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.size = 0
        self.tail = self.Node()
        self.head = self.Node(next=self.tail)
        self.tail.prev = self.head
        self.cache = {} # cache to store key<->node 
        
    def remove_from_pos(self, key: int) -> None:
        node_to_update = self.cache[key]
        node_to_update.prev.next = node_to_update.next  
        node_to_update.next.prev = node_to_update.prev 

    def add_to_end(self, node: Node) -> None:
        node.next = self.tail 
        node.prev = self.tail.prev 
        node.prev.next = node
        self.tail.prev = node 


    def get(self, key: int) -> int:
        val = self.cache.get(key)
        if val is None:
            return -1
        self.remove_from_pos(key)
        self.add_to_end(self.cache[key])
        return val.value 
        

    def put(self, key: int, value: int) -> None:
        print(f"key: {key} value: {value}") 
        if self.cache.get(key) is not None:
            node_to_update = self.cache[key]
            node_to_update.value = value # update value
            self.remove_from_pos(key)
        else:
            node_to_update = self.Node(key=key, value=value)
            # add key-value pair onto the end
            self.size += 1
            if self.size > self.capacity: # exceeds capacity
                # remove least recently used from linked list and cache
                self.cache.pop(self.head.next.key)
                self.head.next = self.head.next.next 
                self.head.next.prev = self.head 
        
        # add to dictionary cache
        self.cache[key] = node_to_update

        # put node at the end
        self.add_to_end(node_to_update)
        
        
