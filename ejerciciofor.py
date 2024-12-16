def años_naciminto():
    años=int(input("ingrese el año en que estamos")) 
    años_naciminto=int(input("ingrese su año de naciminto"))
    edda=años-años_naciminto
    print("tu edad es:",edda)
    for i in range(edda):
         print("valor de la variable edda",i+1)
         time.sleep()
        
#años_naciminto()

def numeros_impares():
     numerso=int(input("ingrese el numeros: "))
     for i in range(1,numerso+1,1):
        print(i, end=",")
        if i==5:
            break;
#numeros_impares()
import time
def reloj():
    relojs=int(input("ingrese el teimpo que desea para"))
    for i in range(1,60,1):
        print(i,"segundos")
        time.sleep(1)
        if i==relojs:
            print("\33[103m"+"tiempo masimo"+"\33[om")
            break;
#reloj()

def sueldo():
    peso_año=float(input("cuanto dinero al año:"))
    tasa_interes=float(input("tasa de interes anual:"))
    cantidad_año=int(input("cuantos años"))
    #for i in range(1,cantidad_año+1):
        #interese=peso_año*(tasa_interes/100)
        #peso_año=peso_año+interese
        #print=(f"en el año {i},el dinero acumulado es:{peso_año:}")
#sueldo()

def triangulo():
    cantidad_de_x =int(input("ingrese la cantidad de *:"))
    for i in range(1,cantidad_de_x +1):
        print("x"*i)
        
#triangulo()

def decubrir_contraseña():
    contraseña="123456789"
    contraseña_ingrsada=""
    intentos_ingresados = int(input("por favor ingresar un numero de intentos: "))
    intentos =1
    while contraseña_ingrsada != contraseña:
        contraseña_ingrsada=str(input("ingrese la contraseña de *:"))
        if contraseña_ingrsada !=contraseña:
            print("la contraseña no conside")
        if contraseña_ingrsada==contraseña:
            print ("contrasña correcta ")
            break
        if intentos == intentos_ingresados:
            print("se lleva al limite de los intentos")
            break
        intentos= intentos+1

#decubrir_contraseña()

def buscador_de_letras ():
    frase=str(input("ingresar la frace que quieras= "))
    letra=str(input("ingrese la letra que quieras buscar= "))
    contador=0
    for i in frase:
        if i==letra:
            contador=contador+1
    print("la letra ",letra,"se repite ",contador," veces")
buscador_de_letras()
   