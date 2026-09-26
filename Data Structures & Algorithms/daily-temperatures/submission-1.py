class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempToDays = [[] for _ in range(101)]
        availTemps = set()

        for i in range(len(temperatures)):
            temp = temperatures[i]
            
            tempToDays[temp].append(i)
        
        for i in range(len(tempToDays)):
            days = tempToDays[i]

            if len(days) > 0:
                availTemps.add(i)

        ans = []
        for i in range(len(temperatures)):
            temp = temperatures[i]

            minDays = 10000
            for item in availTemps:
                if item <= temp:
                    continue
                
                days = tempToDays[item]
                
                lastIndexAppear = days[-1]
                if lastIndexAppear <= i:
                    continue
                
                toContinue = False
                for day in days:
                    if day > i:
                        minDays = min(minDays, day - i)
                        toContinue = True
                        continue
                
                if toContinue:
                    continue
            
            ans.append(0 if minDays == 10000 else minDays)
        
        return ans









