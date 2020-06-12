class evalRPN:
    def __init__(self, arr):
        self.arr = arr

    def evalRPN(self):
        operators = ['+','-','*','/']
        stack = []
        for elem in self.arr:
            if (elem not in operators):
                stack.append(int(elem))
            else:
                a = stack.pop()
                b = stack.pop()
                optr = elem
                if (optr == "+"):
                    stack.append(b + a)
                elif (optr == "-"):
                    stack.append(b - a)
                elif (optr == "*"):
                    stack.append(b * a)
                elif (optr == "/"):
                    stack.append(b / a)
        return stack.pop()

if __name__ == "__main__":
    object = evalRPN(['2','1','+','3','/'])
    print(object.evalRPN())