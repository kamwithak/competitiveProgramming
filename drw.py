class Solution():
    def __init__(self, master_object):
        self.master_object = master_object

if __name__ == "__main__":
    obj = Solution({'name':'kamran','age':'23'})
    print(obj.master_object)
