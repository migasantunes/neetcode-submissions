class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Brute Force
        res = []
        for i, temp in enumerate(temperatures):
            r = i
            
            while r != len(temperatures) and temp >= temperatures[r]:
                r += 1

            if r == len(temperatures):
                res.append(0)
            else:
                res.append(r - i)
        
        return res
        """

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                index, temp = stack.pop()
                res[index] = i - index
            stack.append((i, t))
        return res
