def main():
    nome = input('Informe seu nome completo: ').strip()
    est_civil = int(input('Informe seu estado civil (1 - casado e 2 - solteiro): ').strip())
    if est_civil == 1:
        n_conj = input('Informe o nome completo do seu conjuje: ').strip()
        print('Seu nome tem {} caracteres\nO nome do seu conjuje tem {} caracteres'.format(len(nome), len(n_conj)))
    elif est_civil == 2:
        print(f'Seu nome tem {len(nome)} caracteres')
    else:
        raise ValueError('O valor digitado não corresponde ao exigido')

if __name__ == '__main__':
    main()




