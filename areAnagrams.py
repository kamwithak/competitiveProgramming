class areAnagrams:
    def __init__(self, str1="", str2=""):
        self.str1 = str1
        self.str2 = str2

    def linearSolution(self):
        _dict1 = {} ; _dict2 = {}
        for i in self.str1:
            if (i not in _dict1):
                _dict1[i] = 1
            else:
                _dict1[i] += 1
        for i in self.str2:
            if (i not in _dict2):
                _dict2[i] = 1
            else:
                _dict2[i] += 1
        if (self.dictEqual(_dict1, _dict2)): return True
        return False
    
    def dictEqual(self, _dict1, _dict2):
        if (len(_dict1) != len(_dict2)): return False
        for key in _dict1:
            if (key not in _dict2 or (key in _dict2 and _dict2[key] != _dict1[key])):
                return False
        return True

if __name__ == "__main__":
    obj = areAnagrams("bob", "bbo")
    print(obj.linearSolution())