class Solution:
    def isValid(self, s: str) -> bool:
        mapS = {"]": "[", ")": "(", "}": "{"}
        stack=[]

        for c in s:
            if c in mapS: 
                if stack and stack[-1] == mapS[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False 
        