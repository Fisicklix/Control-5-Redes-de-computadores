import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
#Autor: Gary simken
#Convierte la cadena de bits a una lista
def conversor(cadena):
        lista=cadena.split()
        i=0
        while i<len(lista):
                lista[i]=int(lista[i])
                i+=1
        return lista
#la funcion portadora
#recibe un vector tiempo y la frecuencia
def portadora(t,f):
        portadora=np.cos(2*np.pi*t*f)
        return portadora
#interpola los bits, dado que si solo tenemos un bit solo veriamos un punto
#al pasarlselo a la funcion
#recibe la cadena de bits y la cantidad de puntos que se quieren
#ejemplo recibe bits=(1,0,1) y x=3
#retornaria (1,1,1,0,0,0,1,1,1)

def interpolacion(bits,x):
        i=0
        bitsInterpolados=[]
        while i<len(bits):
                interp=np.ones(x)
                interp=bits[i]*interp
                bitsInterpolados=np.concatenate((bitsInterpolados,interp))
                i+=1
        return bitsInterpolados

#Se recibe la cadena
print("Ingrese los bits separados por un espacio")
print("como en el siguiente ejemplo")
print("         Ej:")
print("            1 0 0 1 1")
print("ADVERTENCIA: En caso de no hacerlo asi, se")
print("             debera volver a ejecutar el programa")
cadena=input("Ingrese los bits: ")

#se convierte  la cadena
bits=conversor(cadena)
cantBits=len(bits)
#y se interpolan
bitsInterpolados=interpolacion(bits,100)
#ahora para el tiempo, como son 100 bits/s los que se transmiten
#creamos un vector desde 0 hasta la cantidad de bits originales
#con la cantidad de datos del tamaño de la interpolacion de bits
t=np.linspace(0,cantBits/100,len(bitsInterpolados))


#Bit 0
f0=100
#Bit 1
f1=200

y=[]
i=0

plt.figure()
ant=bitsInterpolados[i]
#se comienza a armar la figura
while i < len(t):
        #Esta linea grafica una vertical cuando hay un cambio de frecuencia
        #es decir cuando se esta evaluando un bit distinto
        #para asi poder revisar mas comodamente como cambian las frecuencias
        if(ant!=bitsInterpolados[i]):
                plt.axvline(t[i], -1, 1,color="orange")
        #en caso de que se este leyendo un 0, se agrega a una lista
        #el resultado de la funcion portadora con frecuencia 100
        if(bitsInterpolados[i]==0):
                dato=portadora(t[i],f0)
                y.append(dato)

        #y en caso contrario con la de frecuencia 200
        else:
                dato=portadora(t[i],f1)
                y.append(dato)
        ant=bitsInterpolados[i]
        i+=1
#se reconvierte a vector y se grafica
#2 graficos, uno con lineas y otro no
señal=np.array(y)
plt.plot(t,señal)
plt.title("Señal modulada FSK con marcas de cambio")
plt.xlabel("tiempo")
plt.ylabel("modulada")
linea = mlines.Line2D([], [], color='orange',label='Cambio de frecuencia')
plt.legend(handles=[linea],loc='upper right',borderaxespad=0.)

plt.figure()
plt.plot(t,señal)
plt.title("Señal modulada FSK")
plt.xlabel("tiempo")
plt.ylabel("modulada")
plt.show()
