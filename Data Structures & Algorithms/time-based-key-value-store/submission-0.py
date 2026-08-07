class TimeMap:

    def __init__(self):
        self.time_dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key] = [value, timestamp]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.time_dict:
            return ""
        
