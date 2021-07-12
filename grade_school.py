class AddTwoNumbersInBase10():
    def __init__(self, a=[], b=[]):
        self.a = a
        self.length_of_a = len(a)
        self.b = b
        self.length_of_b = len(b)

    def solutionA(self):
        assert self.length_of_a == self.length_of_b
        carry = 0
        res = []
        for i in range(self.length_of_a-1, -1, -1):
            res.append(int((self.a[i] + self.b[i] + carry) % 10))
            carry = (self.a[i] + self.b[i] + carry) / 10
        res.append(int(carry))
        return res[::-1]

if __name__ == '__main__':
    obj = AddTwoNumbersInBase10(
        [1,5,2,1],
        [5,5,3,2]
    )
    # res: 7053
    print(f"Expected Result: {1521+5532}")
    hi = obj.solutionA()
    print(hi)

