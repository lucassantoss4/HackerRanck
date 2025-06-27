def findMedian(arr):
    # Write your code here

    arr_convert = sorted(arr)

    tam_arr = (len(arr)//2)
    resultado = arr_convert[tam_arr]
    print(resultado)

    return resultado