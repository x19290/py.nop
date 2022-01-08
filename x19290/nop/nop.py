def nop(*_, **__):
    r'''
    >>> nop(0, 1, a=2, b=3)
    >>> none(0, 1, a=2, b=3)
    '''
    pass

none = nop
