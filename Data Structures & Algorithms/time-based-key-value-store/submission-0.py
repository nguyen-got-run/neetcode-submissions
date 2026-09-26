class TimeMap:

    def __init__(self):
        self.myMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        pairs = self.myMap.get(key, [])
        pairs.append((value, timestamp))
        self.myMap[key] = pairs
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myMap:
            return ""
        
        pairs = self.myMap[key]
        
        res = ""
        l, r = 0, len(pairs) - 1

        while l <= r:
            m = l + (r-l)//2
            val, valTime = pairs[m]

            if valTime > timestamp:
                r = m - 1
            else:
                res = val
                l = m + 1
        
        return res
