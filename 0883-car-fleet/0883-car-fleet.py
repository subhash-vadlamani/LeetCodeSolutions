class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sorted_data = sorted(zip(position, speed))
        sorted_position, sorted_speed = zip(*sorted_data)

        sorted_position = list(sorted_position)
        sorted_speed = list(sorted_speed)

        sorted_time = []
        list_length = len(sorted_position)

        for i in range(list_length):
            current_car_finish_time = ((target - sorted_position[i]) / sorted_speed[i])
            sorted_time.append(current_car_finish_time)
        
        # Monotonically increasing stack

        fleet_count = 0
        current_max_time = float('-inf')
        for i in range(list_length - 1, -1, -1):
            if sorted_time[i] > current_max_time:
                current_max_time = sorted_time[i]
                fleet_count += 1
        return fleet_count


        # stack = []

        # for i in range(list_length - 1, -1, -1):
        #     while stack and stack[-1] >= sorted_time[i]:
        #         stack.pop()
        #     stack.append(sorted_time[i])
        # fleet_count = len(stack)
        # return fleet_count
        