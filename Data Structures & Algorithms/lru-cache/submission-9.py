class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    #at least constructor was correct for dict and capacity
    def __init__(self, capacity: int):
        self.cache_map = {} #this will map key to node
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0) #initialize dummy nodes
        self.left.next, self.right.prev = self.right, self.left #point dummys to eachother
        #nodes will be populated in between dummys, or the dummy pointers will be updated.

    #at least got the check and return in, but before we knew values were nodes and not numbers.
    def get(self, key: int) -> int:
        if key in self.cache_map:
            #we want the node at cache_map[key] to be removed from LL and then reinsert
            # at the rightmost pos of LL
            self.remove(self.cache_map[key])
            self.insert(self.cache_map[key])

            #accesing cache_map at key returns the node, so .val gets value.
            return self.cache_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        #if the key is in the cache, then our node exists in our list with the same kv.
        if key in self.cache_map:
            #remove the existing kv in our list before adding it
            self.remove(self.cache_map[key])
        #add the node to cache map
        self.cache_map[key] = Node(key,value)
        self.insert(self.cache_map[key])

        if len(self.cache_map) > self.capacity:
            #remove from list and delete lru (left pointer) from cache
            lru = self.left.next
            self.remove(lru)
            del self.cache_map[lru.key]

    #helper functions, would have never thought to use these.
    #remove node from list
    #do this by eliminating the middle node.
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    #insert at right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev
        #prev.next = node
        #self.right.prev = node
        #node.next = self.right
        #node.prev = prev
