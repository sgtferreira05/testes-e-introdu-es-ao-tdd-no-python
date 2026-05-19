from calculadora import soma

# print(soma(10, 20))       
# print(subtracao(10, 5))    
# print(multiplicacao(10, 5))  
# print(divisao(10, 5))

try:
    print(soma(10, '20'))  # Isso deve gerar um erro
except AssertionError as e:
    print(f"Erro: {e}")
