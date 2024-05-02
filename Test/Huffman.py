import Arbol

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
    
def contarPalabras(Direccion):

    Diccionario = {};
    Archivo = leerArchivo(Direccion)
    for i in Archivo:

        try: 

            Diccionario[i] += 1

        except:
            Diccionario[i] = 1

    return Diccionario

def swap(Diccionario, A, B):

    Temporal = Diccionario[A]
    Diccionario[A] = Diccionario[B];
    Diccionario[B] = Temporal

def particion(Diccionario, Inicio, Final):

    pivote = Diccionario[Inicio][1];
    i = Inicio + 1

    for j in range(Inicio, Final + 1):
        if(pivote > Diccionario[j][1]):
            swap(Diccionario, i, j)
            i += 1

    swap(Diccionario, Inicio, i - 1)

    return i - 1
            
def quicksort(Diccionario, Inicio, Final):

    if(Final >= Inicio):

        Pivote = particion(Diccionario, Inicio, Final)
        quicksort(Diccionario, Inicio, Pivote - 1)
        quicksort(Diccionario, Pivote + 1, Final)

def comprimir(Direccion):

    Palabras = list(contarPalabras(Direccion).items())
    quicksort(Palabras, 0, len(Palabras) - 1);

    Contenido = leerArchivo(Direccion)
    arbolHuffman.comprimir(Direccion, Contenido, Palabras)

def descomprimir():

    arbolHuffman.descomprimir()

arbolHuffman = Arbol.arbolHuffman()
