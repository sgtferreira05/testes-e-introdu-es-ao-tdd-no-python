def soma(x,y):
    '''
    Soma x e y, onde x e y devem ser números (int ou float).
    >>> soma(10, 20)
    30
    >>> soma(-15, 25)
    10
    >>> soma(3.5, 2.5)
    6.0
    >>> soma('10', 20)
    Traceback (most recent call last):
    AssertionError: O primeiro argumento deve ser um número
    '''



    # Geralmente assert é para outros desenvolvedores e não para o usuário final, por isso é mais comum usar TypeError ou ValueError
    assert isinstance(x, (int, float)), "O primeiro argumento deve ser um número"
    assert isinstance(y, (int, float)), "O segundo argumento deve ser um número"
    return x + y


def subtracao(x,y):
    '''
    Subtrai y de x, onde x e y devem ser números (int ou float).
    >>> subtracao(10, 5)
    5
    >>> subtracao(25, 15)
    10
    >>> subtracao(3.5, 2.5)
    1.0
    >>> subtracao('10', 5)
    Traceback (most recent call last):
    AssertionError: O primeiro argumento deve ser um número
    '''
    assert isinstance(x, (int, float)), "O primeiro argumento deve ser um número"
    assert isinstance(y, (int, float)), "O segundo argumento deve ser um número"
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)