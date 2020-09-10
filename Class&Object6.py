# %%
# method overloading


class overload:
    def greeting(self, name=None):
        if name is not None:
            print("welcome" + name)
        else:
            print('Welcomeeeeee!!!!!!')


obj = overload()
obj.greeting()
obj.greeting('Swaraj')

# %%


class demo:
    result = 0

    def add(self, instanceof=None, *args):
        if instanceof == 'int':
            self.result = 0
        if instanceof == 'str':
            self.result = ''
        for i in args:
            self.result = self.result+i
        return self.result


d1 = demo()
print(d1.add('int', 10.5, 20, 30))
print(d1.add('str', 'i', 'love', 'python'))
