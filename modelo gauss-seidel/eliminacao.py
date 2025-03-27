def eliminacao_gauss(A, B):
    n = len(A)
    
    # Passo 1: Montando a matriz aumentada [A|B]
    for i in range(n):
        A[i].append(B[i])  # Adiciona o vetor B como a última coluna de A
    
    # Passo 2: Eliminação de Gauss
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError("Pivô zero detectado, trocar de linha")
        
        # Eliminação para as linhas abaixo da linha i
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]
            for k in range(i, n + 1):
                A[j][k] -= fator * A[i][k]
    
    # Passo 3: Substituição retroativa
    X = [0 for _ in range(n)]  # Inicializa o vetor solução X com zeros
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += A[i][j] * X[j]  # Soma os termos multiplicados
        X[i] = (A[i][n] - soma) / A[i][i]  # Resolve para X[i]
    
    return X

# Matriz A e vetor B para o sistema linear A * X = B
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
B = [8, -11, -3]

# Chama a função de Eliminação de Gauss
X = eliminacao_gauss(A, B)

# Exibe a solução
print("Solução do sistema:",X)