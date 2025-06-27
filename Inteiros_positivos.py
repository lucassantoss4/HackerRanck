def miniMaxSum(arr):
    # Write your code here       
    arr_organize = arr.sort()
    contador_1 = arr[:-1]
    contador_2 = arr[1:]

    dicio_sum = {
        'Lista Minino ': contador_1,
        'Lista Maximo ': contador_2
    }

    soma_mim = soma_maxi =0
    for lista, valor in dicio_sum.items():
        if lista == 'Lista Minino ':
            for v in valor:
                soma_mim+=v

        elif lista == 'Lista Maximo ':
            for m in valor:
                soma_maxi += m

    lista_final = [soma_mim, soma_maxi]


    print(f'{soma_mim} {soma_maxi}')