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
tablero = []

for i in range(0,8):
    for j in range(0,8):
        tablero.append(' ')

def colocar_negras():
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