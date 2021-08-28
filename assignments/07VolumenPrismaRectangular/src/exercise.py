def area(b,a):
    ar=b*a
    return ar

def volumen(area,p):
    vol=area(b,a)*p
    return vol

def main():
    #escribe tu código abajo de esta línea
    b=float(input("Dame la base: "))
    a=float(input("Dame la altura: "))
    p=float(input("Dame la profundidad: "))
    print("El volumen del prisma es:", volumen(area,p))


if __name__=='__main__':
    main()
