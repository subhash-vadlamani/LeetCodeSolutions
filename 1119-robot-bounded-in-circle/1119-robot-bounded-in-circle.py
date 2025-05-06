class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position_dict = dict()
        position_dict[(0,0)] = 1
        current_position = (0, 0)
        current_increment = (0, 1)

        def calculate_new_increment(current_increment, movement_direction):
            """
                4 possible states of current increment
                (1, 0)
                (0, 1)
                (-1, 0)
                (0, -1)

                for all these 4 cases, based on the movement type, we decide the new increment
            """
            new_increment = None

            if current_increment == (1, 0):
                if movement_direction == "L":
                    new_increment = (0, 1)
                elif movement_direction == "R":
                    new_increment = (0, -1)
                    
            elif current_increment == (0, 1):
                if movement_direction == "L":
                    new_increment = (-1, 0)
                elif movement_direction == "R":
                    new_increment = (1, 0)
            elif current_increment == (-1, 0):
                if movement_direction == "L":
                    new_increment = (0, -1)
                elif movement_direction == "R":
                    new_increment = (0, 1)
            else:
                if movement_direction == "L":
                    new_increment = (1, 0)
                elif movement_direction == "R":
                    new_increment = (-1, 0)
            
            return new_increment
        
        complete_instructions = instructions * 4
        # print(complete_instructions)

        for current_char in complete_instructions:
            if current_char == "G":
                temp = current_position
                current_position = tuple(a + b for a, b in zip(temp, current_increment))
                # print(current_position)
                position_dict[current_position] = 1 + position_dict.get(current_position, 0)
            
            else:
                current_increment = calculate_new_increment(current_increment, current_char)
        
        return True if current_position == (0, 0) else False



        