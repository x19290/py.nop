def nullint(*_, **__):
    return 0


def nulltuple(*_, **__):
    return ()


def nulllist(*_, **__):
    return []


def nullgen(*_, **__):
    r'''
    >>> nullgen(0, 1, a=2, b=3).__next__()
    Traceback (most recent call last):
    StopIteration
    '''

    yield from ()
