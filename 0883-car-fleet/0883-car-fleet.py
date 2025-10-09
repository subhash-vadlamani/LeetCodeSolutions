class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key = lambda x:-x[0])
        stack = []

        for pos, current_speed in cars:
            t = (target - pos)/current_speed

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
        