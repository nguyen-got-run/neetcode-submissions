class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        n = len(positions)
        pairs = []
        for i in range(n):
            pos, vel = positions[i], speeds[i]
            pairs.append((pos, vel))
        
        pairs.sort(key=lambda x: -x[0])
        st = []
        for p, s in pairs:
            t = (target - p) / s
            if not st:
                st.append(t)
            else:
                if t > st[-1]: st.append(t)

        return len(st)  

