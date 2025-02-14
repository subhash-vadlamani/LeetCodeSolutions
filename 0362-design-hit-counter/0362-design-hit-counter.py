class HitCounter:

    def __init__(self):
        self.hit_list = []
        

    def hit(self, timestamp: int) -> None:
        self.hit_list.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:

        lower_bound = timestamp - 300 + 1

        left, right = 0, len(self.hit_list)

        while left < right:
            mid = (left + right) // 2
            if self.hit_list[mid] < lower_bound:
                left = mid + 1
            else:
                right = mid
        
        return len(self.hit_list) - left
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)