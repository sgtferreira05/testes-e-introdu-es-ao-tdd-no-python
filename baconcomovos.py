"""
1 - Receber um valor inteiro do usuário
2 - Verificar se o valor é multiplo de 3 e 5:
    Se for multiplo de 3 e 5, imprimir "Bacon com ovos"
3 - Se for multiplo de 3:
    imprimir "Bacon"
4 - Se for multiplo de 5:
    imprimir "Ovos"
5 - Se não for multiplo de 3 ou 5:
    imprimir sem café
"""

def bacon_com_ovos(valor):
    assert isinstance(valor, int), "O valor deve ser um inteiro"

    if valor % 3 == 0 and valor % 5 == 0:
        return "Bacon com ovos"
    elif valor % 3 == 0:
        return "Bacon"
    elif valor % 5 == 0:
        return "Ovos"
    else:
        return "Sem café"
    