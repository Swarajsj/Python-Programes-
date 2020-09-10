# %%
# super class()


class demo:
    a = 0
    b = 0
    c = 0

    def __init__(self, a1, b1, c1):
        self.a = a1
        self.b = b1
        self.c = c1

    def dis(self):
        print(self.a, self.b, self.c)


class newdemo(demo):
    d = 0

    def __init__(self, a1, b1, c1, d1):
        self.d = d1
        super().__init__(a1, b1, c1)

    def dis(self):
        print(self.a, self.b, self.c, self.d)


b1 = demo(100, 200, 300)
print('Content of base class :)')
b1.dis()
d1 = newdemo(10, 20, 30, 40)
print('Content of derived class :)')
d1.dis()
