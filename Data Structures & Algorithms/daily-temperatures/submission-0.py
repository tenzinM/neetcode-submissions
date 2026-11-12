class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outputArr = [0] * len(temperatures)
        stack = [] # pair [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                outputArr[stackIndex] = i - stackIndex
            stack.append((temp,i))
        return outputArr
            
        
        