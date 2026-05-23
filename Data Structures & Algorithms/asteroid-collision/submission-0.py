class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if not stack:
                stack.append(asteroids[i])
            else:
                prev = stack[-1]
                crt = asteroids[i]
                if prev > 0 and crt < 0:
                    if abs(prev) > abs(crt):
                        pass
                    elif abs(prev) == abs(crt):
                        stack.pop()
                    else:
                        stack.pop()
                        continue
                else:
                    stack.append(crt)
            i += 1
        return stack
                        
                    
