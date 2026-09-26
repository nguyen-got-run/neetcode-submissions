class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = []
        speedAtPosAr = [0] * (max(position) + 1)

        for i in range(len(position)):
            speedAtPosAr[position[i]] = speed[i]
        
        for pos in range(len(speedAtPosAr)-1, -1, -1):
            sp = speedAtPosAr[pos]
            if sp == 0: continue
    
            
            numTurnsToTarget = float(target - pos) / sp
            stk.append(numTurnsToTarget)

            if len(stk) < 2:
                continue
            
            if stk[-1] <= stk[-2]:
                stk.pop()
        
        return len(stk)
        
            

        