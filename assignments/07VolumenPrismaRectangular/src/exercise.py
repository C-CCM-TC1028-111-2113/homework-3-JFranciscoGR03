
def volumen(b,h,p):
    v=b*h*p
    return v

def main():
    #escribe tu código abajo de esta línea
    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    p=float(input("Dame la profundidad: "))
    print("El volumen del prisma es:", volumen(b,h,p))


if __name__=='__main__':
    main()
