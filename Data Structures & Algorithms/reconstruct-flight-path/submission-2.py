
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # Reverse sort so smallest destination is at the end
        tickets.sort(reverse=True)

        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(airport):
            while adj[airport]:
                nei = adj[airport].pop()
                dfs(nei)

            # Add airport AFTER using all outgoing tickets
            res.append(airport)

        dfs("JFK")

        return res[::-1]

