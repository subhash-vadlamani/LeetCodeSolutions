class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        """
            The list stores the seat number that each friend sits in.
        """
        number_of_friends = len(times)
        seated_chair_list = [-1] * number_of_friends
        occupied_chairs_list = [0] * number_of_friends
        for i in range(0, number_of_friends):
            new_list = []
            new_list.append(times[i][0])
            new_list.append(times[i][1])
            new_list.append(i)
            times[i] = new_list
        """
            'occupied_chairs_list' stores whether or not a chair at the index 'i' 
            is occupied or not. '0' indicates that the chair is not occupied.
            '1' indicates that the chair is occupied.
        """
        # print(times)
        times_sorted_arrival = sorted(times, key=lambda x:x[0])
        times_sorted_depature = sorted(times, key=lambda x:x[1])

        """
            The above lists store the times based on the arrival or depature time
        """
        i = 0
        j = 0
        """
            'i' represents the index in the 'times_sorted_arrival' list.
            'j' represents the index in the 'times_sorted_depature' list.
        """

        last_depature_time = times_sorted_depature[-1][1]

        print(times_sorted_arrival)

        for t in range(1, last_depature_time + 1):

            if j < number_of_friends:
                count = 0
                for k in range(j, number_of_friends):
                    earliest_departing_friend = times_sorted_depature[k]
                    earliest_departing_friend_departing_time = earliest_departing_friend[1]
                    if earliest_departing_friend_departing_time == t:
                        earliest_departing_friend_arrival_time = earliest_departing_friend[0]
                        earliest_departing_friend_number = earliest_departing_friend[2]

                        earliest_departing_friend_seat_number = seated_chair_list[earliest_departing_friend_number]
                        occupied_chairs_list[earliest_departing_friend_seat_number] = 0
                        count += 1
                    else:
                        break
                j += count
            
            if i < number_of_friends:
                earliest_arriving_friend = times_sorted_arrival[i]
                earliest_arriving_friend_arriving_time = earliest_arriving_friend[0]
                if earliest_arriving_friend_arriving_time == t:
                    earliest_arriving_friend_number = earliest_arriving_friend[2]
                    best_available_seat_number = occupied_chairs_list.index(0)
                    seated_chair_list[earliest_arriving_friend_number] = best_available_seat_number
                    occupied_chairs_list[best_available_seat_number] = 1
                    i += 1
        return seated_chair_list[targetFriend]






        