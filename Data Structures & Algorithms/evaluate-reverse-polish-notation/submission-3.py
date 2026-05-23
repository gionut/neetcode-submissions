class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": lambda x: x[1] + x[0], \
        "-": lambda x: x[1] - x[0], \
        "*": lambda x: x[1] * x[0], \
        "/": lambda x: int(x[1] / x[0]) }
        for t in tokens:
            if t in operators:
                x = (stack.pop(), stack.pop())
                stack.append(operators[t](x))
            else:
                stack.append(int(t))
        return stack[0]