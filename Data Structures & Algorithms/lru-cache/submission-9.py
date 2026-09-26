class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

    def reinsert(self, key: int) -> None:
        if key not in self.cache: return
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val

    def update(self, key: int) -> None:
        ordered_keys = list(self.cache.keys())
        if len(ordered_keys) > self.cap:
            first = ordered_keys[0]
            del self.cache[first]
        elif key in self.cache:
            self.reinsert(key)


    def get(self, key: int) -> int:
        if key in self.cache:
            return self.reinsert(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value

        self.update(key)


