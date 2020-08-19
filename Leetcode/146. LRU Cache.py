
"""# 146. LRU Cache

https://leetcode.com/problems/lru-cache/
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = []
        self.values = []
        self.capacity = capacity
        self.least_used_key = None 


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print ("Get",key)

        if key in self.keys :
            return key
        else:
            return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.get(key) ==-1:
            if len(self.keys) +1 > self.capacity:
                self.least_used_key = self.keys
                self.keys.pop(-1)
                self.values.pop(-1)      
            if  self.get(key) ==-1:                
                self.keys.append(key)
                self.values.append(value)
        print ("Put",key, "Updated keys=",self.keys)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache =LRUCache( 2  );

print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))       #// returns 1
print(cache.put(3, 3))    #// evicts key 2
print(cache.get(2))      #// returns -1 (not found)
print(cache.put(4, 4))  # // evicts key 1
print(cache.get(1))       #// returns -1 (not found)
print(cache.get(3))       #// returns 3
print(cache.get(4))      # // returns 4
