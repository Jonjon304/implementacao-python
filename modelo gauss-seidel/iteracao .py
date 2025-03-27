import numpy as np

def gauss_seidel(A, B, erro=0.4, max_iter=100):
    # Inicialização
    n = len(A)  # Número de variáveis
    x = np.zeros(n)  # Vetor solução inicial (pode ser qualquer valor, normalmente começa com zeros)

    # Iterações
    for k in range(max_iter):
        x_novo = np.copy(x)  # Faz uma cópia do vetor solução

        for i in range(n):
            soma = 0
            # Soma sobre as variáveis já calculadas (i.e., variáveis na iteração anterior)
            for j in range(n):
                if j != i:
                    soma += A[i][j] * x[j]

            # Atualiza o valor de x[i] usando o método de Gauss-Seidel
            x_novo[i] = (B[i] - soma) / A[i][i]

        # Verifica a convergência, comparando a solução atual com a anterior
        erro_atual = np.max(np.abs(x_novo - x))  # Erro máximo entre as iterações
        x = np.copy(x_novo)

        # Se o erro for menor que o erro tolerado, podemos parar
        if erro_atual < erro:
            print(f"Convergência alcançada em {k+1} iterações.")
            return x

    print("Número máximo de iterações atingido.")
    return x

# Exemplo de uso com um sistema de equações
A = np.array([
    [10, 2, -1],
    [-3, -6, 2],
    [1, 1, 5]
], dtype=float)

B = np.array([6, -2, 7], dtype=float)

# Chama a função de Gauss-Seidel
solucao = gauss_seidel(A, B, erro=0.4, max_iter=100)

print("Solução:",solucao)