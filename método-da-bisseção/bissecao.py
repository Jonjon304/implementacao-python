import math

def f(x):
    return 

def bissecao(func, a, b, tol, max_iter):
    
    if func(a) * func(b) >= 0:
        print("Erro: A função deve ter sinais opostos nos extremos do intervalo inicial.")
        return None, 0

    print("Iteração |    a     |    b     |    c     |   f(c)   | |b - a|")
    print("------------------------------------------------------------------")

    for i in range(max_iter):
        c = (a + b) / 2
        print(f"{i+1:^9} | {a:^8.4f} | {b:^8.4f} | {c:^8.4f} | {func(c):^8.4f} | {abs(b - a):^7.4f}")

        if abs(b - a) < tol:
            return c, i + 1

        if func(c) == 0:
            return c, i + 1
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c

    print(f"\nO método não convergiu dentro de {max_iter} iterações.")
    return None, max_iter

if __name__ == "_main_":
    # Permitir ao usuário inserir a função (uma forma simples usando eval, tenha cuidado com entradas maliciosas)
    funcao_str = input("Digite a função f(x) (use 'math.' para funções matemáticas): ")
    try:
        def f_usuario(x):
            return eval(funcao_str)
    except:
        print("Erro ao interpretar a função inserida.")
        exit()

    # Permitir ao usuário inserir os parâmetros iniciais
    while True:
        try:
            a_inicial = float(input("Digite o limite inferior inicial (a): "))
            b_inicial = float(input("Digite o limite superior inicial (b): "))
            break
        except ValueError:
            print("Por favor, digite valores numéricos.")

    # Permitir ao usuário inserir o critério de parada
    while True:
        try:
            tolerancia = float(input("Digite a tolerância desejada: "))
            if tolerancia <= 0:
                print("A tolerância deve ser um valor positivo.")
            else:
                break
        except ValueError:
            print("Por favor, digite um valor numérico.")

    # Definir o número máximo de iterações
    max_iteracoes = 100  # Um valor razoável

    # Executar o método da bisseção com a função fornecida pelo usuário
    raiz, iteracoes = bissecao(f_usuario, a_inicial, b_inicial, tolerancia, max_iteracoes)

    if raiz is not None:
        print(f"\nRaiz aproximada encontrada: {raiz:.8f}")
        print(f"Número de iterações: {iteracoes}")
