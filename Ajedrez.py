import sys

piezas_bl={
    'torre': chr(0x2656),
    'caballo': chr(0x2658),
    'alfil': chr(0x2657),
    'reina': chr(0x2655),
    'rey': chr(0x2654),
    'peon': chr(0x2659)
}
piezas_ne={
    'torre': chr(0x265C),
    'caballo': chr(0x265E),
    'alfil': chr(0x265D),
    'reina': chr(0x265B),
    'rey': chr(0x265A),
    'peon': chr(0x265F)
}
#tablero = []
tablero = [
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ']
]

def colocar_negras():
    
    global tablero
    global piezas_ne

    #Colocar piezas negras
    tablero[0][0] = piezas_ne['torre']
    tablero[0][1] = piezas_ne['caballo']
    tablero[0][2] = piezas_ne['alfil']
    tablero[0][3] = piezas_ne['reina']
    tablero[0][4] = piezas_ne['rey']
    tablero[0][5] = piezas_ne['alfil']
    tablero[0][6] = piezas_ne['caballo']
    tablero[0][7] = piezas_ne['torre']
    #Colocar peones negros
    for i in range(0,8):
        tablero[1][i]=piezas_ne['peon']
    
def colocar_blancas():

    global tablero

    #Colocar piezas blancas
    tablero[7][0] = piezas_bl['torre']
    tablero[7][1] = piezas_bl['caballo']
    tablero[7][2] = piezas_bl['alfil']
    tablero[7][3] = piezas_bl['reina']
    tablero[7][4] = piezas_bl['rey']
    tablero[7][5] = piezas_bl['alfil']
    tablero[7][6] = piezas_bl['caballo']
    tablero[7][7] = piezas_bl['torre']
    #Colocar peones blancos
    for i in range(0,8):
        tablero[6][i]=piezas_bl['peon']

def guardar_tablero(f,cont):

    global tablero

    #Pintar todas las posiciones del tablero
    f.write(str(cont))
    f.write(" Tablero:")
    f.write("\n")
    for i in range(0,8):
        f.write(" ")
        for j in range(0,8):
            f.write(tablero[i][j])#.encode('utf8'))
        f.write("\n")

def mover_pieza():
    
    global tablero

    salir = False

    while(salir==False):
        print("Que pieza quieres mover?")
        fila_o= int(input('Fila: '))
        columna_o= int(input('Columna: '))
        if(tablero[fila_o][columna_o]==' '):
            print("Esta casilla esta vacia")
        else:
            print("Donde la quieres mover?")
            fila_d= int(input('Fila: '))
            columna_d= int(input('Columna: '))
            if(tablero[fila_d][columna_d]==' '):
                tablero[fila_d][columna_d]=tablero[fila_o][columna_o]
                tablero[fila_o][columna_o]=' '
                salir=True
            else:
                print("La casilla esta ocupada")

def pintar_tablero(nombre,mov):
    fi = open(nombre+".txt","r",encoding='utf-8')
    impr = False

    while(True):
        linea = fi.readline()
        if(str(mov)==linea[0:1]):
            impr=True
        if(linea[0:1] != " " and str(mov)!=linea[0:1]):
            impr=False
        if(impr==True):
            print(linea)
        if not linea:
            break

    fi.close()


def main():

    global tablero
    
    colocar_negras()
    colocar_blancas()

    nombre= input('Como quieres que se llame el archivo en el que se guarde tu partida?: ')

    fi = open(nombre+".txt","w",encoding='utf-8')

    guardar_tablero(fi,1)

    fin = False
    i=2

    while(fin==False):
        quiere_jugar= input('Desea seguir jugando?: ')
        if(quiere_jugar == "S" or quiere_jugar =="s"):
            mover_pieza()
            guardar_tablero(fi,i)
            i=i+1
        elif(quiere_jugar == "N" or quiere_jugar =="n"):
            fin=True
        else:
            print("La respuesta debe ser una S o una N")

    fi.close()
    print("--*PARTIDA FINALIZADA*--")
    mov= int(input('Que movimiento deseas ver?: '))
    if(mov<i):
        pintar_tablero(nombre,mov)
    else:
        print("Ese  movimiento no existe")

if __name__ == "__main__":
    main()