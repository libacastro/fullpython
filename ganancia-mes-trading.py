# cuenta=input("tamaño de la cuenta ")
# cuenta=int(cuenta)

# porcent=input("ganacia semanal ")
# porcent=float(porcent)

# i=0
# while i<4:

#    resul=cuenta*porcent
#    total=resul+cuenta
#    i=i+1
#    print("semana",i,"ganacia",resul,"total",total)
#    cuenta=total



def run():
   cuenta = int(input('Ingresa el tamaño de tu cuenta: '))
   porcentaje_ganancia = float(input('Ingresa el porsentaje que aspiras ganar a la semana: '))
   
   for i in range(1,5):
      ganancia = cuenta*porcentaje_ganancia
      cuenta = cuenta+ganancia
      print(f'Al terminar la semana {i} la ganancia es de {ganancia} y el nuevo monto de la cuenta es {cuenta}')

if __name__ == '__main__':
   run()
   
