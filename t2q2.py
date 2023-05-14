def exibeFibonacci(quantidade):
    primeiro = 0
    segundo  = 1
    cont = 2
    print(f'{primeiro}, {segundo}', end='')

    while cont < quantidade:
        proximo = primeiro + segundo
        primeiro = segundo
        segundo = proximo
        
        print(f', {proximo}', end='')
        cont += 1


def main():
    quantidade = int(input())

    exibeFibonacci(quantidade)


if __name__ == '__main__':
    main()