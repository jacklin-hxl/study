
def b(x):
    return x


class property_:

    @b
    def a(self):
        return 1


test = property_()
print(test.a)