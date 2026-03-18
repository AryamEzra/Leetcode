class MyHashMap:

    def __init__(self):
        self.myhashmap = {}
        

    def put(self, key: int, value: int) -> None:
        self.myhashmap[key] = value
        

    def get(self, key: int) -> int:
        if key in self.myhashmap:
            return self.myhashmap[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        if key in self.myhashmap:
            self.myhashmap[key] = -1

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)