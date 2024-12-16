
def suma_dos_valores(sumando1,sumando2):
    global resultado
    resultado = sumando1 + sumando2
    print (resultado)
    return resultado
#suma_dos_valores(4,8)
#print("primera suma ")
#print(resultado)
#suma_dos_valores(1,3)
#rint ("segundo suma")
#print(resultado)

#def pitagoras (A,B):
    #global c
    #c=(A**2+B**2)**0.5
    #return c
#pitagoras(4,5)
#print("pitagoras",c)

def despejo_X():
    global X
    a=int(input("ingrese el valor de a="))
    b=int(input("ingrese el valor de b="))
    X=(a-b)/2
    print("el valoer de x es:",X)
    return X

#despejo_X()

def multiplicacion_x():
    global resultado_multiplicacion
    print("multiplicacion")
    a= bool(input("ingrese el valor de a="))
    b=bool (input("ingrese el valor de b="))
    c=bool (input("ingrese el valor de c= "))
    resultado_multiplicacion=a and b and c 
    print (resultado_multiplicacion)

#multiplicacion_x()

def pitagoras_funcion_suma(): 
    global resultado_pitagoras 
    a=int (input("ingrese el valo de a="))
    b=int (input("ingrese el valor de b="))
    a2=a**2
    b2=b**2
    suma=suma_dos_valores(a2,b2)
    resultado_pitagoras= suma**0.5  
    print("el resultado de pitagoras es", resultado_pitagoras)
    #return resultado_pitagoras

#pitagoras_funcion_suma()
def contra_letra():
    global resultado_contador
    palabra= str(input("ingrese la palabra a contar"))
    letra=str(input("ingrese la letra a contra "))
    resultado_contar = palabra.count(letra) 
    print("la cantidad de palabra ",letra,"es",resultado_contar)
    print("palabra separaba ppor letra=,",list(palabra))
    return resultado_contar
#contra_letra()

def selecionar_ganador():
    global ganador
    jugadores=set(jugador1,jugador2)
    jugador1=["piedra","papel","tigerra"]
    print("si pierde o gana ")
    jugador2=["piedra","papel","tigerra"]
    print("si pierdr o gan ")
    selecionar_ganador= jugadores(jugador1,jugador2)
    print("separe el ganador con su elecion",selecionar_ganador, "es",ganador)
    print("ganador",(selecionar_ganador))
    return selecionar_ganador
    #elif(jugador1=="pedra",and jugador2=="piedra",)("jugador1"==tijerra,and  "jugador2"==papel)
#finalista_ganador=()

import time
def ejercicio ():
        palabra=set (input("por favor injrese"))
        cantidad=set(input("por favor ingresa la cantidad de veces:"))
        for i in range(cantidad):
             print("valor de la variable i",i)
             time.sleep(2)
             print(palabra)
#return palabra
#ejercicio1()

#import time
def edda ():
    edda=int(input("ingesar tu edda"))
    for i in range(edda):
         print("valor de la variable edda",i)
         time.sleep(2)
         print("tu edad es:",edda)
#edda()


def años_naciminto():
    años=int(input("ingrese el año en que estamos")) 
    años_naciminto=int(input("ingrese su año de naciminto"))
    edda=años-años_naciminto
    print("tu edad es:",edda)
    for i in range(edda):
         print("valor de la variable edda",i+1)
         time.sleep()
        
#años_naciminto()