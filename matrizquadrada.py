def diagonalDifference(arr):
    n = len(arr)
    soma_primaria = 0
    soma_secundaria = 0

    # Usar 'for i in range(n)' é mais seguro que um 'while' manual
    # 1. Ele nunca será um loop infinito.
    # 2. A variável 'i' serve perfeitamente como nosso índice de linha.
    for i in range(n):
        
        # Lógica para a diagonal primária (esquerda-direita)
        # Pega o elemento onde linha e coluna são iguais: arr[i][i]
        soma_primaria += arr[i][i]
        
        # Lógica para a diagonal secundária (direita-esquerda)
        # Pega o elemento onde a coluna é (n - 1 - i)
        soma_secundaria += arr[i][n - 1 - i]
        
    return abs(soma_primaria - soma_secundaria)