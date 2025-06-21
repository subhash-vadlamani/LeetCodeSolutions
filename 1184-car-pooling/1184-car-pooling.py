class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        """
            I think it will help if I think of this like a number line

            
        """
        events = []

        for p, s, e in trips:
            events.append((s, 1, p))
            events.append((e, 0, -p))

        events.sort()

        current = 0

        for t, e, delta in events:
            current += delta
            if current > capacity:
                return False
        return True

        