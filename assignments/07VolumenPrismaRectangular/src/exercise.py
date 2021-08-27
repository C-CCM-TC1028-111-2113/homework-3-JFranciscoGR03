
def area(b,a):
    ar=b*a
    return float(ar)

def volumen(area,p):
    vol=area(b,a)*p
    return vol

b=float(input("Dame la base: "))
a=float(input("Dame la altura: "))
p=float(input("Dame la profundidad: "))

def main(volumen):
    print("El volumen del prisma es:", volumen(area,p))
    return print

main(volumen)


if __name__=='__main__':
    main()
