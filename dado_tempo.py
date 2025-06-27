s='01:01:00AM'

def timeConversion(s):
    # Write your code here
    s_hora = s[:2]
    s_minuto = s[3:5]
    s_segundos = s[6:8]

    valoridacao = s[8:10]


    if valoridacao == 'AM':
        if s_hora == '12':
            horario = f'00:{s_minuto}:{s_segundos}'

        else:
            horario = f'{s_hora}:{s_minuto}:{s_segundos}'

    else:
        if s_hora == '12':
            horario = f'24:{s_minuto}:{s_segundos}'

        else:
            hora_convert = int(s_hora)
            horario = f'{hora_convert+12}:{s_minuto}:{s_segundos}'
            # print(hora_convert)

    return(horario)

print(timeConversion(s))