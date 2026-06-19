class MyHashMap:

    def __init__(self):
        self.hashmap=[]

    def put(self, key: int, value: int) -> None:
        for j in self.hashmap:
            if j[0]==key:
                j[1]=value
                return
        self.hashmap.append([key,value])
                

    def get(self, key: int) -> int:
        for j in self.hashmap:
            if j[0]==key:
                return j[1]
        return -1
        
    def remove(self, key: int) -> None:
        for j in self.hashmap:
            if j[0]==key:
                self.hashmap.remove(j)
                break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)