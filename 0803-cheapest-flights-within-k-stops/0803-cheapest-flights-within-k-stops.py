from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Construct Graph

        g = defaultdict(list)
        for flight_from, flight_to, price in flights:
            g[flight_from].append([flight_to, price])
        
        minHeap = [[0, src, k+1]] # [price_to_reach_the_particular_node, node, stops_left]
        # visit = set()
        min_price = float('inf')
        visited = {}
        while minHeap:
            current_price, current_node, current_stops_left = heapq.heappop(minHeap)

            # print("{}, {}, {}".format(current_price, current_node, current_stops_left))

            if current_node == dst:
                return current_price
            
            # Skip if we've visited this node with more or equal stops left
            if (current_node, current_stops_left) in visited and visited[(current_node, current_stops_left)] <= current_price:
                continue
            
            visited[(current_node, current_stops_left)] = current_price
            
            # visit.add(current_node)
            if current_stops_left > 0:
                # explore the neighbors of the current_node

                for nei, price in g[current_node]:
                    heapq.heappush(minHeap, [current_price + price, nei, current_stops_left - 1])
        
        return -1

        