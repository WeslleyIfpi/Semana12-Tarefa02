def calculaH(n):
    h = 0
    for i in range(1 , n+1):
        h += 1/i    
    return h

def main():
    entrada = int(input())

    h = calculaH(entrada)

    print(f'{h:.4f}')


if __name__ == "__main__":
    main()