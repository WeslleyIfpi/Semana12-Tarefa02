def calcFatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcFatorial(numero - 1)


def main():
    numero = int(input())
    fatorial = calcFatorial(numero)
    print(f'{fatorial}')



if __name__ =='__main__':
    main()