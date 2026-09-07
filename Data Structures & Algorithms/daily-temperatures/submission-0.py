class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        process = []
        final = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while process and temperatures[i] > temperatures[process[-1]]:
              previous = process.pop()
              day = i - previous
              final[previous] = day
            
            process.append(i)
        
        return final