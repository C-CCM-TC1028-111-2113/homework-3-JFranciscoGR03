
def area(b,h):
    a=b*h
    return a

def main():
    #escribe tu código abajo de esta línea
    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    print("El área del rectángulo es:", area(b,h))

if __name__=='__main__':
    main()
