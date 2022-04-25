def ordem(a, b, c):
    primeiro = min(a, b, c)
    terceiro = max(a, b, c)
    if primeiro == a and terceiro == b:
        segundo = c
        return f'{primeiro}, {segundo}, {terceiro}'
    elif primeiro == b and terceiro == c:
        segundo = a
        return f'{primeiro}, {segundo}, {terceiro}'
    else:
        segundo = b
        return f'{primeiro}, {segundo}, {terceiro}'

def main():
    n1 = float(input('Informe o 1º valor: ').strip())
    n2 = float(input('Informe o 2º valor: ').strip())
    n3 = float(input('Informe o 3º valor: ').strip())
    print(ordem(n1, n2, n3))

if __name__ == '__main__':
    main()