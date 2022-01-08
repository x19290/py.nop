def identity(y, *_, **__):
    r'''
    >>> identity(False, 0, 1, a=2, b=3)
    False
    '''

    return y


def strictidentity(y):
    r'''
    >>> strictidentity(False, 0)
    Traceback (most recent call last):
    TypeError: strictidentity() takes 1 positional argument but 2 were given

    >>> strictidentity(False, a=2)
    Traceback (most recent call last):
    TypeError: strictidentity() got an unexpected keyword argument 'a'
    '''

    return y
