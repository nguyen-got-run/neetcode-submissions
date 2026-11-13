class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ctMap, h = {}, []

        for task in tasks:
            if task not in ctMap:
                ctMap[task] = 0
            ctMap[task] += 1
        
        for task in ctMap:
            h.append((-ctMap[task], task))
        
        heapq.heapify(h)
        # choose Queue class because it helps to pop left in O(1)
        ans, q = 0, deque()

        while h or q:
            ans += 1

            if h:
                ct, task = heapq.heappop(h)
                
                ct += 1 # negative, so +1 instead of -1
                heal = ans + n

                # push to buffer queue if it's still active
                if ct: q.append((ct, task, heal))
            
            if q:
                ct, task, heal = q[0]
                # the first item in buffer queue is good to be processed
                # so we pop from the queue and add back to the heap
                if heal == ans:
                    q.popleft()
                    heapq.heappush(h, (ct, task))
        
        return ans

