# Esta versao deve ser aceita pela plataforma

def timeConversion(s):
    # Extrai as partes da string de tempo
    hora_str = s[:2]
    minuto_segundo = s[2:8] # Pega minutos e segundos juntos
    periodo = s[8:10]       # AM ou PM

    if periodo == 'PM':
        # Se for PM e a hora for 12, a hora fica 12 (meio-dia)
        if hora_str == '12':
            return f"12{minuto_segundo}"
        # Para outras horas PM (01 a 11), some 12
        else:
            hora_int = int(hora_str) + 12
            return f"{hora_int}{minuto_segundo}"
            
    else: # Periodo eh 'AM'
        # Se for AM e a hora for 12, vira 00 (meia-noite)
        if hora_str == '12':
            return f"00{minuto_segundo}"
        # Para outras horas AM (01 a 11), a hora ja esta correta
        else:
            return s[:8] # Retorna a parte HH:MM:SS da string original