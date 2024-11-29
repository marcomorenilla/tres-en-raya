# Juego tres en raya
# La dinámica de juego es la siguiente:
# Se crea un array bidimensional 3x3
# Se llena con los números
#   Se repite mientras la condición sea falsa:
#       Se inicializa tablero
#       Se pregunta al j1 dónde quiere poner la ficha
#       Se añade el número a array posiciones
#       Se pregunta al j2 dónde quiere poner la ficha
#       Se añade el número a array posiciones
#       Se coloca array posiciones de ambos jugadores en tablero
#       Una vez hayan pasado los 3 primeros movimientos hay que mover las fichas
#       Se comprueba si alguno de los dos ha cumplido:
#           - 3 fichas consecutivas horizontales o
#           - 3 fichas consecutivas verticales o
#           - 3 fichas consecutivas en diagonal

# Condiciones de victoria
#
# Horizontales -> tablero[0][0], tablero[0][1], tablero[0][2] -> if tablero[i][j] = 'x' or 'o'
# Verticales -> tablero[0][0], tablero[1][0], tablero[2][0] -> if tablero[j][i] = 'x' or 'o'
# Diagonal -> tablero[0][0], tablero[1][1], tablero[2][2] -> if i == j tablero[i][j] = 'x' or 'o' 
# Diagonal-inv -> tablero[0][2], tablero[1][1], tablero [2][0] -> if j == cont if tablero[i][cont] = 'x' or 'o'


print()
print('\t\t__________')
print('\t\tBienvenido')
print('\t\t----------')

#zona declarativa
j1 = {
    'nombre':'j1',
    'ficha': 'X',
    'posiciones': [],
    'ganador': False
}

j2 = {
    'nombre':'j2',
    'ficha': 'O',
    'posiciones': [],
    'ganador': False
}
jugada = 0    
tablero = [[1,2,3],[4,5,6],[7,8,9]]

#introdue nombre a los jugadores
def inicializar_nombres():
    j1['nombre']=(input('Introduce el nombre del primer jugador:\nNombre: ')) 
    j2['nombre']=(input('Introduce el nombre del segundo jugador:\nNombre: ')) 

#añade números a las posiciones del tablero
def inicializar_tablero(tablero):
    contador = 1
    for i in range(3):
        for j in range(3):
            tablero[i][j] = contador
            contador+=1
            
#imprime el tablero por pantalla            
def visualizar(tablero):
    print()
    for i in range(3):
        print('\t\t ___ ___ ___')
        print('\t\t|   |   |   |')
        print(f'\t\t| {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]} |')
        print('\t\t|   |   |   |')  
    print('\t\t --- --- ---')
    print()
    
#coloca el número entrado por pantalla en la lista posiciones del jugador        
def preguntar_posicion(jugador):
    posiciones_tablero = [0]
    posiciones_tablero += j1['posiciones'] + j2['posiciones']
    posicion = int(input(f'{jugador["nombre"]} introduce la posición en la que poner la ficha:\nPosición: '))

    while(index_of(posicion,posiciones_tablero)):
        posicion = int(input(f'{jugador["nombre"]} la posición está ocupada introduce una nueva posición:\nPosición: '))
     
    jugador['posiciones'].append(posicion)

#comprobar posiciones del tablero en una lista, si no existe retorna False
def index_of(pos, lista):
    existe = False
    if len(lista)>0:
        for i in lista:
            if pos == i:
                existe = True
    return existe

#coloca la lista del jugador en el tablero        
def colocar_ficha(jugador, tablero):
    contador = 1
    index = 0
    pos_ordenada = sorted(jugador['posiciones'])
    #print('jugada ordenada',pos_ordenada,sep=' ')
    for i in range(3): 
        for j in range(3):
            if index < len(jugador['posiciones']):
                pos = pos_ordenada[index]
            if pos == contador:
                    tablero[i][j] = jugador['ficha']
                    index+=1
            contador+=1
            
#cambia la lista de posiciones del jugador    
def mover_ficha(jugador):
    print(f'{jugador["nombre"]} ,tus fichas están colocadas en', jugador['posiciones'], sep = ' ')
    ficha = int(input('¿Qué ficha quieres mover?: '))
    nueva_ficha = int(input('¿Dónde quieres mover la ficha?: '))
    nueva_lista = []
    for i in jugador['posiciones']:
        if i == ficha:
            nueva_lista.append(nueva_ficha)
        else:
            nueva_lista.append(i)
    print('nueva_lista',nueva_lista,sep=' ')
    jugador['posiciones']=nueva_lista
    
#método para comprobar si el jugador ha ganado e interrumpir el bucle
def comprobar_resultados(jugador, tablero):

    cont_diagonal = 0
    cont_diagonal_inv = 0
    contador = 2
    
    for i in range(3): 
        cont_horizontal = 0
        cont_vertical = 0
        for j in range(3):  

            if tablero[i][j] == jugador['ficha']:
                cont_horizontal+=1
                if cont_horizontal == 3:
                    jugador['ganador']= True
            if tablero[j][i] == jugador['ficha']:
                cont_vertical += 1
                if cont_vertical == 3:
                    jugador['ganador']=True
            if i==j and tablero[i][j] == jugador['ficha']:
                cont_diagonal+=1
            if j == contador and tablero[i][contador] == jugador['ficha']:
                cont_diagonal_inv+=1
                if contador > 0:
                    contador-=1
    
    if cont_diagonal == 3 or cont_diagonal_inv ==3:
        jugador['ganador']=True

#dinámica de juego         
inicializar_nombres()
while  not j1['ganador'] and not j2['ganador']:
    
    visualizar(tablero)
    if jugada<3:
        #preguntar j1 dónde quieres poner la pieza
        preguntar_posicion(j1)
        #colocar la pieza j1
        colocar_ficha(j1,tablero)
        #mostrar tablero
        visualizar(tablero)
        #repetir para j2
        preguntar_posicion(j2)
        colocar_ficha(j2,tablero)
        comprobar_resultados(j1,tablero)
        comprobar_resultados(j2,tablero)
        jugada+=1
    else:
        inicializar_tablero(tablero)
        mover_ficha(j1)
        colocar_ficha(j1,tablero)
        colocar_ficha(j2,tablero)
        visualizar(tablero)
        inicializar_tablero(tablero)
        mover_ficha(j2)
        colocar_ficha(j1,tablero)
        colocar_ficha(j2,tablero)
        comprobar_resultados(j1,tablero)
        comprobar_resultados(j2,tablero)
    if j1['ganador']:
        print()
        print(f'¡ {j1["nombre"]} ha ganado la partida!')
    elif j2['ganador']:
        print()
        print(f'¡ {j2["nombre"]} ha ganado la partida!')

#despedida
print()
print('\t\t_________________')
print('\t\tGracias por jugar')
print('\t\t-----------------')     

