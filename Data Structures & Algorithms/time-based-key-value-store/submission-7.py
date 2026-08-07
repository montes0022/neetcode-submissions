class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_dict:
            self.time_dict[key] = []
        
        self.time_dict[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_dict:
            return ""
        arr = self.time_dict[key]

        l = 0
        r = len(arr)-1
        res = ""

        while l <= r:
            m = (l+r) // 2
            rightmost = m - 1

            if arr[m][1] <= timestamp:
                res =  arr[m][0]
                l = m +1
            else:
                r = m -1
        return res


