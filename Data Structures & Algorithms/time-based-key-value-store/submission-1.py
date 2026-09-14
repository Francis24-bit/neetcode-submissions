class TimeMap:
    # 1. Data structure: Dictionary → List → [value, timestamp]
    # 2. Access the values: self.book[key][mid][0] → value; self.book[key][mid][1] → timestamp
    # 3. Possible answer: When mid timestamp < target timestamp, save the current value as possible_answer, then search right. A later valid candidate can overwrite it.

    def __init__(self):
        self.book = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.book:
            self.book[key] = []
        self.book[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.book:
            return ""
        
        left = 0
        right = len(self.book[key]) - 1
        possible_answer = ""

        while left <= right:
            mid = left + (right - left) // 2
            
            if self.book[key][mid][1] == timestamp:
                return self.book[key][mid][0]
            
            elif self.book[key][mid][1] < timestamp:
                possible_answer = self.book[key][mid][0]
                left = mid + 1
            
            else:
                right = mid - 1

        return possible_answer