def digito_par(num, pares = 0):
    centena = num // 100
    dezena = (num % 100) // 10
    unidade = (num % 100) % 10
    if centena % 2 == 0:
        pares += 1
    if dezena % 2 == 0:
        pares += 1
    if unidade % 2 == 0:
        pares += 1
    return f'O número {num} tem {pares} dígitos pares'

def main():
    numero = int(input('Informe um número entre 100 e 999: ').strip())
    print(digito_par(numero))

if __name__ == '__main__':
    main()