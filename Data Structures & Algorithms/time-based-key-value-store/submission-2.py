class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_dict:
            self.time_dict[key].append([value,timestamp])
        else:
            self.time_dict[key] = [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_dict:
            return ""

        arr = self.time_dict[key]
        timestamps = []

        for item in arr:
            timestamps.append(item[1])

        return ""
        
