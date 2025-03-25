class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
            1. Rectangles do not overlap
            2. Either 2 horizontal(y = k) or 2 vertical lines(x = k); where k is a constant
            3. Each of the 3 resulting sections formed by the cuts contain at least one rectangle
            4. Each rectangle belongs to exactly one section(i.e, the lines should not divide the rectangle)

        """

        """
            eg 1: 
            Interval question?
            y interval of the rectangles
            y_interval_list = [[0, 2], [2, 4], [2, 3], [4, 5]]
            say, we have a sorted list
            sorted_y_interval_list = [[0, 2], [2, 3], [2, 4], [4, 5]]

            For this example, lets construct the x interval list too
            sorted_x_interval_list = [[0, 2], [0, 4], [1, 5], [3, 5]]
        """

        """
            eg 2:
            sorted_x_interval_list = [[0, 1], [0, 2], [2, 3], [3, 4]]
        """

        """
            from the given list, construct 
            sorted_x_interval_list
            sorted_y_interval_list
        """

        """
            eg 4: 
            [[0,0,1,4],[1,0,2,3],[2,0,3,3],[3,0,4,3],[1,3,4,4]]
            sorted_x_interval_list = [[0, 1], [1, 2], [1, 4], [2, 3], [3, 4]]
        """
        x_interval_list = []
        y_interval_list = []
        for a, b, c, d in rectangles:
            x_interval_list.append([a, c])
            y_interval_list.append([b, d])
        
        # sort the lists
        sorted_x_interval_list = sorted(x_interval_list, key = lambda x:(x[0], x[1]))
        sorted_y_interval_list = sorted(y_interval_list, key = lambda y:(y[0], y[1]))

        # check for vertical lines
        vertical_line_count = 0
        horizontal_line_count = 0
        prev_x_list = sorted_x_interval_list[0]
        prev_y_list = sorted_y_interval_list[0]
        interval_length = len(sorted_x_interval_list)
        for i in range(1, interval_length):
            if vertical_line_count == 2 or horizontal_line_count == 2:
                break
            
            current_x_list = sorted_x_interval_list[i]
            current_y_list = sorted_y_interval_list[i]

            if prev_x_list[1] <= current_x_list[0]:
                vertical_line_count += 1
            else:
                current_x_list[1] = max(current_x_list[1], prev_x_list[1])

            if prev_y_list[1] <= current_y_list[0]:
                horizontal_line_count += 1
            else:
                current_y_list[1] = max(current_y_list[1], prev_y_list[1])
            
            prev_x_list = current_x_list
            prev_y_list = current_y_list
        
        if vertical_line_count == 2 or horizontal_line_count == 2:
            return True
        return False
        
        



        