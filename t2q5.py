def eh_primo(numero):
    divisores = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            divisores += 1
    
    if divisores == 2:
        return True
    else:
        return False


def numerosPrimos(numero1, numero2): 
    maior = numero1 if numero1 > numero2 else numero2
    menor = numero1 if numero1 < numero2 else numero2

    for i in range (menor, maior+1):
        if eh_primo(i):
            print(i)
        


def main():
    numero1 = int(input())
    numero2 = int(input())

    numerosPrimos(numero1, numero2)



if __name__ == '__main__':
    main()