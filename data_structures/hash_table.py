class HashTable:
    data = []
    def __init__(self, size):
        self.data = [[] for _ in range(size)]
    
    def put(self, key, value):
        hash_code = self.hash_func(key)
        slots = self.data[hash_code]
        is_existing = False
        for i, kv in enumerate(slots):
            k,v = kv
            if k == key:
                is_existing = True
                slots[i] = (key, value)
                break
        if not is_existing:
            slots.append((key, value))

    def remove(self, key):
        hash_code = self.hash_func(key)
        slots = self.data[hash_code]
        for i, kv in enumerate(slots):
            k,v = kv
            if k == key:
                del slots[i]
                return
        print("key not found")


    def get(self, key):
        hash_code = self.hash_func(key)
        slots = self.data[hash_code]
        for i, kv in enumerate(slots):
            k,v = kv
            if k == key:
                return v
        return None

    def hash_func(self, key):
        return hash(key)%len(self.data)
    def get_full_table(self):
        return self.data


h = HashTable(10)
h.put("a", 1)
h.put("b", 2)
h.remove("c")
print(h.get("a"))
print(h.get("b"))
print(h.get("f"))
print(h.get_full_table())
