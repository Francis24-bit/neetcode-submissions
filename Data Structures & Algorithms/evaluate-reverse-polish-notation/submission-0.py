class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        bag = []

        for element in tokens:
            if element not in "+-*/":
                bag.append(int(element))
            else:
                n1 = bag.pop()
                n2 = bag.pop()
                if element == "+":
                    result = n2 + n1
                elif element == "-":
                    result = n2 - n1
                elif element == "*":
                    result = n2 * n1
                elif element == "/":
                    result = int(n2 / n1)
                bag.append(result)

        return bag[0]
