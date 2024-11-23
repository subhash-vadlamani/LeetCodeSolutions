class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
            Break the problems into 2 parts:
            1. Rotate the matrix
            2. Apply the effect of gravity

            I can also apply the effect of gravity initially too
            by pusing the stones as right as possible.
        """

        def push_right(my_list, my_list_len):
            """
            Accepts an input list containing rocks ('#'), obstacles ('*'), and empty spaces ('.').
            Pushes rocks as far right as possible without crossing obstacles or moving obstacles.

            Args:
                my_list (list): The input list.
                my_list_len (int): Length of the input list.

            Returns:
                list: The modified list with rocks pushed to the right.
            """

            # Start with the most right available index as the last position
            most_right_available_index = my_list_len - 1

            for i in range(my_list_len - 1, -1, -1):
                current_element = my_list[i]

                if current_element == '#':
                    # Move the rock to the most_right_available_index if possible
                    if my_list[most_right_available_index] == '.':
                        my_list[most_right_available_index] = '#'
                        my_list[i] = '.'
                        most_right_available_index -= 1
                    else:
                        # If the position isn't empty, update most_right_available_index
                        most_right_available_index -= 1
                elif current_element == '*':
                    # Reset the most_right_available_index to just before the obstacle
                    most_right_available_index = i - 1

            return my_list
        def rotate(matrix):
            """
            Rotates an m * n matrix by 90 degrees clockwise.

            Args:
                matrix (list[list[int]]): The input m * n matrix.

            Returns:
                list[list[int]]: The rotated n * m matrix.
            """
            # Reverse the rows of the matrix
            matrix.reverse()
            
            # Transpose the reversed matrix
            rotated_matrix = []
            for col in range(len(matrix[0])):  # Iterate over columns of the original matrix
                new_row = [matrix[row][col] for row in range(len(matrix))]  # Create a new row from the column
                rotated_matrix.append(new_row)
            
            return rotated_matrix
        # def rotate(matrix):
        #     """
        #         Accepts the box and rotates it by 90 Degrees clockwise
        #     """

        #     l, r = 0, len(matrix) - 1

        #     while l < r:
        #         for i in range(r - l):
        #             top, bottom = l, r

        #             # Save the topLeft value
        #             topLeft = matrix[top][l + i]

        #             # move the bottom left to the top left
        #             matrix[top][l + i] = matrix[bottom - i][l]

        #             # move the bottom right to the bottom left
        #             matrix[bottom - i][l] = matrix[bottom][r - i]

        #             # move the top right to the bottom right
        #             matrix[bottom][r - i] = matrix[top + i][r]

        #             # move the stored topLeft to the top right
        #             matrix[top + i][r] = topLeft
                
        #         r -= 1
        #         l += 1
            
        #     return matrix
        
        m = len(box)
        n = len(box[0])

        for i in range(m):
            box[i] = push_right(box[i], n)
        
        print(box)
        
        rotated_box = rotate(box)

        return rotated_box


        