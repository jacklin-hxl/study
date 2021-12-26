import threading

class local:
    """
    {get_ident(): {key: value}}
    """

    def __init__(self):
        object.__setattr__(self, "_stroage", {})

    def __setattr__(self, key, value):
        values = self._stroage.get(threading.get_ident(), {})
        values[key] = value
        self._stroage[threading.get_ident()] = values

    def __getattr__(self, key):
        values = self._stroage.get(threading.get_ident(), {})
        return values[key]

local1 = local()
local1.a = 1

def worker1():
    local1.a = 2
    print("in thread: " + threading.current_thread().name)
    print(str(local1.a).center(10, "#"))

def worker2():
    local1.a = 3
    print("in thread: " + threading.current_thread().name)
    print(str(local1.a).center(10, "#"))

thread1 = threading.Thread(target=worker1, name="hxl")
thread2 = threading.Thread(target=worker2, name="jieni")
thread1.start()
thread2.start()

print("main thread " + str(local1.a))


