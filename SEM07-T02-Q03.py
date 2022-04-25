def dig_impar(num):
    dezena = num // 10
    unidade = num % 10
    if dezena % 2 == 0 and unidade % 2 == 0:
        return f'Nenhum dígito é ímpar'
    elif dezena % 2 == 0 or unidade % 2 == 0:
        return f'Apenas um dígito é ímpar'
    else:
        return f'Os dois dígitos são ímpares'

def main():
    numero = int(input('Digite um número entre 10 e 99: ').strip())
    print(dig_impar(numero))

if __name__ == '__main__':
    main()