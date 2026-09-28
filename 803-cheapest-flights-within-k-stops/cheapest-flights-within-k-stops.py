from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        
        graph = [[] for _ in range(n)]

        for start, end, price in flights:
            graph[start].append((end, price))

        
        queue = deque()
        queue.append((src, 0, 0))

   
        cost = [float('inf')] * n
        cost[src] = 0

        while queue:

            city, current_cost, stops = queue.popleft()

            if stops > k:
                continue

            for next_city, price in graph[city]:

                new_cost = current_cost + price

                if new_cost < cost[next_city]:
                    cost[next_city] = new_cost

                    queue.append(
                        (next_city, new_cost, stops + 1)
                    )

        if cost[dst] == float('inf'):
            return -1

        return cost[dst]