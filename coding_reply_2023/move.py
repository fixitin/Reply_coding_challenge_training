

"""
Funzione per controllare se la cella è al margine della matrice.
Il meccanismo controlla se una delle due coordinate è uguale
alla minima grandezza della matrica o alla massima grandezza
della matrice.
"""
def is_border(x, y,r_min,r_max,c_min,c_max):
    if (x == r_min or x == r_max-1) or (y == c_min or y == c_max-1):
        return True
    
    return False


"""
Semplice serie di moveset 4 direzioni che permettono il
movimento di un passo nella matrice
"""
def move(x,y,step):
    
    match(step):
        case "UP":
            return  x - 1, y
        
        case "DOWN":
            return x + 1, y
        
        case "RIGHT":
            return x, y + 1
        
        case "LEFT":
            return x, y - 1
        
"""
Semplice serie di moveset come nel metodo move,
in questo caso si considera la matrice una sfera di karnaugh
e quindi si considera il movimento in 3 dimensioni possibile
"""     
def move_is_border(x,y,step,r_min,r_max,c_min,c_max):
    
    match(step):
        case "UP":
            return  r_max, y
        
        case "DOWN":
            return r_min, y
        
        case "RIGHT":
            return x, c_min
        
        case "LEFT":
            return x, c_max
    
    
M = [
    [1,2,3,4,5,6],
    [7,8,9,10,11],
    [12,13,14,15],
    [16,17,18,10]
    ]

x = 3
y = 0
print(M[x][y])
print(is_border(x,y,0,3,0,3))
print(move_is_border(x,y,"LEFT",0,3,0,3))