def diferencas_divididas(x, y):
    """Calcula a tabela de diferenças divididas."""
    n = len(y)
    tabela = [list(y)]
    for i in range(1, n):
        nova_coluna = []
        for j in range(n - i):
            delta_y = tabela[i - 1][j + 1] - tabela[i - 1][j]
            delta_x = x[j + i] - x[j]
            nova_coluna.append(delta_y / delta_x)
        tabela.append(nova_coluna)
    return [coluna[0] for coluna in tabela]

def interpolacao_newton(x, y, ponto):
    """Calcula o valor interpolado no 'ponto' usando o método de Newton."""
    n = len(x)
    if len(y) != n:
        raise ValueError("As listas de x e y devem ter o mesmo tamanho.")
    if n == 0:
        return 0

    coeficientes = diferencas_divididas(x, y)
    resultado = coeficientes[0]
    termo = 1
    for i in range(1, n):
        termo *= (ponto - x[i - 1])
        resultado += coeficientes[i] * termo
    return resultado

def obter_lista_float(mensagem):
    """Obtém uma lista de números float inseridos pelo usuário, com tratamento de erro."""
    while True:
        entrada = input(mensagem)
        try:
            valores_str = entrada.split(',')
            valores = [float(v.strip()) for v in valores_str]
            return valores
        except ValueError:
            print("ERRO: Insira números válidos separados por vírgula.")

# Obter os pontos x e y do usuário com validação
while True:
    x_pontos = obter_lista_float("Digite os valores de X separados por vírgula: ")
    y_pontos = obter_lista_float("Digite os valores de Y separados por vírgula: ")
    if len(x_pontos) == len(y_pontos) and x_pontos:
        break
    else:
        print("Erro: O número de valores de X deve ser igual ao número de valores de y e as listas não podem estar vazias.")

# Obter os pontos para interpolação com validação
pontos_interpolacao = obter_lista_float("Digite os pontos onde você quer interpolar:  ")

# Realizar a interpolação para cada ponto
for ponto in pontos_interpolacao:
    valor_interpolado = interpolacao_newton(x_pontos, y_pontos, ponto)
    print(f"O valor interpolado em x = {ponto} é: {valor_interpolado}")