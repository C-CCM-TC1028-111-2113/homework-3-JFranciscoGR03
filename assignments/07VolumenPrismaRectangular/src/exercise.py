def area(b,h):
    a=b*h
    return a

def volumen(area,p):
    v=area*p
    return v

def main():
    #escribe tu código abajo de esta línea
    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    p=float(input("Dame la profundidad: "))
    print("El volumen del prisma es:", volumen)


if __name__=='__main__':
    main()
