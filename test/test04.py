
def a(z=1, x=2, c=3):
    print(z)
    print(x)
    print(c)

class A():

    def __init__(self):
        self.q = 1
        self.w = 2
        self.e = 3
        d = 1

    @staticmethod
    def c(q=8, w=9, e=0):
        print(q)
        print(w)
        print(e)

d = {"z":2, "c":4, "x":5}




if __name__ == "__main__":
    # c(**d)
    a = A()
    d = a.__dict__
    print(d)
    # a.c(**d)