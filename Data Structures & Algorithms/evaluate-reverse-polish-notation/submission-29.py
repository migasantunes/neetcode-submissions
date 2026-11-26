class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ['+', '-', '*', '/']

        stack = []

        for token in tokens:
            if token in operators:
                x = int(stack.pop())
                y = int(stack.pop())
                if token == '+':
                    stack.append(str(y + x))
                elif token == '-':
                    stack.append(str(y - x))
                elif token == '*':
                    stack.append(str(y * x))
                elif token == '/':
                    stack.append(str(int(y / x)))
                continue
            stack.append(token)
        
        return int(stack.pop())