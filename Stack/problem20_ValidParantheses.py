class Solution:
    def isValid(self, s: str) -> bool:
        #first: create a lookup hashmap, initialize stack
        #second: loop through string, if i is closing element, pop from stack if the last element is opening elemnt of that element
        #third: if its an opening element then add to the stack
        #fourth: finally, if stack is empty after the loop return true
        buffer = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for i in s:
            if i in buffer:
                if stack and stack[-1]==buffer[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True