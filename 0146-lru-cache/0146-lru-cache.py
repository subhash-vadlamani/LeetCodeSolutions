from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        """
            1. Initialize a queue
            2. store the capacity
            3. initialize a key-value store
        """
        self.my_dict = dict()
        self.capacity = capacity
        self.queue = deque()
        

    def get(self, key: int) -> int:
        if key in self.my_dict:
            self.queue.remove(key)
            self.queue.append(key)
            return self.my_dict[key]

        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.queue.remove(key)
            self.queue.append(key)
            self.my_dict[key] = value
        else:
            if len(self.queue) == self.capacity:
                popped_key = self.queue.popleft()
                self.my_dict.pop(popped_key)
            self.queue.append(key)
            self.my_dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)