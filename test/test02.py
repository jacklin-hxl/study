class Test(object):
    #私有方法
    def __test2(self):
        print("私有方法__test2方法")
    #普通方法
    def test(self):
        print("普通方法test")
    #普通方法
    def _test1(self):
        print("普通方法_test1方法")
        #可以在类内部调用私有方法
        self.__test2()
t = Test()
t.test()
t._test1()
t.__test2
#t.__test2()和t.test2()#调用的时候会报错