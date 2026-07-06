class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            if c == "+":
                s.append(s.pop() + s.pop())
            elif c == "-":
                a, b = s.pop(), s.pop()
                s.append(b - a)
            elif c == "*":
                s.append(s.pop() * s.pop())
            elif c == "/":
                a, b = s.pop(), s.pop()
                s.append(int(float(b) / a))
            else:
                s.append(int(c))
        return s[0]