# a = [1,1,2,2,3,4,3,2,1]

def lonelyinteger(a):
    # Write your code here
    valor_unico = int()
    dicio = {
        'Valores repetidos': a,
        'Valor Unitario': valor_unico
    }

    for v in dicio['Valores repetidos']:
        for v in dicio['Valores repetidos']:
            contador = dicio['Valores repetidos'].count(v)
            if contador == 1:
                dicio['Valor Unitario'] = v
                break


    return(dicio['Valor Unitario'])