class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #first: append the element if an operand, else pop the element to perform relevant operation
        #second: return the only element present in stack after the loop

        stack = []

        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif i == "*":
                stack.append(stack.pop()*stack.pop())
            elif i == "/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(i))
        return stack[0]