class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if top == "(" and c != ")" or top == "[" and c != "]" or top == "{" and c != "}":
                    return False
                elif not stack:
                    return True
                else:
                    stack.pop()
        return len(stack) == 0
