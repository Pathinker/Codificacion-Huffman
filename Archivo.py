import os
from tkinter import *
from tkinter import ttk

def generarDiccionario():
    
    Diccionario = {}

    for i in range(256):
        
        Diccionario[chr(i)] = i

    Diccionario["’"] = 256
    print(Diccionario)

    return Diccionario;   

def leerArchivo(Archivo):
    
    try:

        with open (Archivo, "r", encoding="utf8") as Documento:

            Contenido = Documento.read()
            return Contenido
        
    except FileNotFoundError:

        print("Archivo no Encontrado");
        return None;
    
def contarPalabras():

    
    #Diccionario = generarDiccionario();
    Contador = 0
    Diccionario = {};
    Archivo = leerArchivo("C:/Users/GuzDa/OneDrive/Documentos/Algoritmos/Huffman/Gullivers_Travels.txt")
    Lista = []

    for i in range(len(Diccionario)):

        Lista.append(0);

    for i in Archivo:

        print(i);

        try: 

            Lista[Diccionario[i]] += 1;

        except:

            Lista.append(1)
            Diccionario[i] = Contador

            Contador += 1

    print(Diccionario);
    print(Lista);      
    
    return Lista

def bubleSort(Arreglo, Diccionario):

    for i in len(Arreglo):
        for j in len(Arreglo - 1):

            if(Arreglo[i] > Arreglo[i + 1]):
                Temporal = Arreglo[i + 1]
                temporalDiccionario = Arreglo[i + 1];

#print(leerArchivo("C:/Users/GuzDa/OneDrive/Documentos/Algoritmos/Huffman/Gullivers_Travels.txt"));    
#contarPalabras()

#

Ventana = Tk();
Frame = ttk.Frame(Ventana, padding=50)
Frame.grid()
ttk.Button(Frame, text = "Abrir").grid(column=0, row=0)
Ventana.mainloop()

# os.getcwd() Retornar Directorio
# os.mkdir() Crear carpeta

#1614
#btn = ttk.Button(Frame)
#print(btn.configure().keys()) Me regresa todas las posibles configuraciones o elementos a editar de cada label

#Progres Bar (Mostrar de manera interactiva el progreso del usuario)

#Diccionario = generarDiccionario() 
#print(Diccionario["’"]);
