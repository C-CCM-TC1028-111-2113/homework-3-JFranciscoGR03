
def main():
    #escribe tu código abajo de esta línea
    
def es_bisiesto(year):
    if year%4==0:
        return True
    elif year%100==0:
        return False
    elif year%400==0:
        return True
    else:
        return False
    
year=int(input())
         
print(es_bisiesto(year))

if __name__=='__main__':
    main()
