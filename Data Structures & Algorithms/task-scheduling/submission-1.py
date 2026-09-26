class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMap = {}

        for task in tasks:
            if task not in countMap:
                countMap[task] = 0
            
            countMap[task] += 1
        
        maxHeap = []
        for task in tasks:
            if task not in countMap:
                continue
            
            count = countMap[task]
            
            maxHeap.append((-count, task))
            del countMap[task]
        
        heapq.heapify(maxHeap)
        processQ = deque()
        cur_time = 0

        while maxHeap or processQ:
            cur_time += 1
    
            if maxHeap:
                negcount, task = heapq.heappop(maxHeap)
            
                next_avail_time = cur_time + n
                negcount += 1
                
                if negcount:
                    processQ.append((next_avail_time, negcount, task))
            
            if processQ:
                avail_time, negcount, task = processQ[0]
                if avail_time == cur_time:
                    processQ.popleft()
                    heapq.heappush(maxHeap, (negcount, task))

        
        return cur_time



