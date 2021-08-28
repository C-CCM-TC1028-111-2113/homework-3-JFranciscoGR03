
def numMax(pliegos,plumones):
    tarPli=pliegos*12
    tarPlu=plumones*35
    if tarpli>tarplu:
        print("El número máximo de tarjetas que se pueden hacer es:", tarPlu)
    else:
        print("El número máximo de tarjetas que se pueden hacer es:", tarPli)

def main():
   #escribe tu código debajo de esta línea     
    pliegos=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones=int(input("Dame la cantidad de plumones: "))
    numMax(pliegos,plumones)

if __name__=='__main__':
    main()
