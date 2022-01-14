


class TestMain(object):
    # des = TestDes()

    class TestDes(object):
        def __init__(self, a):
            pass

        def __get__(self, instance, owner):
            print(instance, owner)
            return 'TestDes:__get__'

class B:

    # @TestMain.TestDes
    def a(self):
        print("pppppp")

    a = TestMain.TestDes(a)
class C(B):

    def c(self):
        return self.a()
# def a(**kwargs):
#     a = kwargs.get("l")
#     print(a)
#
#
# class A:
#     def __init__(self, a):
#         self.a = a
#
#     def __get__(self, obj, cls):
#         print(obj)
#
# @A
# def b():
#     print(b)
#
if __name__ == "__main__":
    B.a()