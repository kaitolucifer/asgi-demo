from greenlet import greenlet


def test1():
    print(1)
    gr2.switch()
    print('test1 done')


def test2():
    print(2)
    gr1.switch()


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
