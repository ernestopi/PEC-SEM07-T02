def signo(dia, mes):
    if (21<= dia <= 31 and mes == 3) or (1 <= dia <= 19 and mes == 4):
        return f'Seu signo é de Áries'
    elif (20 <= dia <= 31 and mes == 4) or (1 <= dia <= 20 and mes == 5):
        return f'Seu signo é de Touro'
    elif (21 <= dia <= 31 and mes == 5) or (1 <= dia <= 21 and mes == 6):
        return f'Seu signo é de Gêmeos'
    elif (22 <= dia <= 31 and mes == 6) or (1 <= dia <= 22 and mes == 7):
        return f'Seu signo é de Câncer'
    elif (23 <= dia <= 31 and mes == 7) or (1 <= dia <= 22 and mes == 8):
        return f'Seu signo é de Leão'
    elif (23 <= dia <= 31 and mes == 8) or (1 <= dia <= 22 and mes == 9):
        return f'Seu signo é de Virgem'
    elif (23 <= dia <= 31 and mes == 9) or (1 <= dia <= 22 and mes == 10):
        return f'Seu signo é de Libra'
    elif (23 <= dia <= 31 and mes == 10) or (1 <= dia <= 21 and mes == 11):
        return f'Seu signo é de Escorpião'
    elif (22 <= dia <= 31 and mes == 11) or (1 <= dia <= 21 and mes == 12):
        return f'Seu signo é de Sagitário'
    elif (22 <= dia <= 31 and mes == 12) or (1 <= dia <= 19 and mes == 1):
        return f'Seu signo é de Capricórnio'
    elif (20 <= dia <= 31 and mes == 1) or (1 <= dia <= 18 and mes == 2):
        return f'Seu signo é de Aquário'
    elif (19 <= dia <= 31 and mes == 2) or (1 <= dia <= 20 and mes == 3):
        return f'Seu signo é de Peixes'

def main():
    dia = int(input('Informe seu dia de nascimento: ').strip())
    mes = int(input('Informe seu mês de nascimento: ').strip())
    ano = int(input('Informe seu ano de nascimento: ').strip())
    print(signo(dia, mes))

if __name__ == '__main__':
    main()