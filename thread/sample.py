from threading import Thread


def simple_print(i):
    print(i)


def sample_1():
    threads = []
    for i in range(1000):
        t = Thread(target=simple_print, args=(i, ))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Hello world")


def sample_2():
    class SimplePrinter(Thread):
        def __init__(self, v):
            super(SimplePrinter, self).__init__()
            # Thread.__init__(self)
            self.v = v
        def run(self):
            print(self.v)

    threads = []
    for i in range(1000):
        t = SimplePrinter(i)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Hello world")


if __name__ == '__main__':
    sample_1()
    sample_2()

