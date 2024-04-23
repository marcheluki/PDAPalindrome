palabra = "babab"

def d(i, s): #ESTADO Q1
    s2 = s[:] #copia del stack
    print(i,s2) #imprime el índice y el stack
    if i == len(palabra) and len(s2)==0: #llega a caso base (i = palabra y stack esta vacio)
        return True #es palíndromo
    if i >= len(palabra): #si i es mayor o igual a la longitud de la palabra
        return False #no es palíndromo
    if s2 and (s2[-1] == palabra[i]): #TRANSICION, si el elemento del top of stack es igual a la letra actual
        s2.pop() #quita el último elemento de la lista
        return d(i+1,s2)  #pasa a la siguiente letra
    return False #si no se cumple la condición anterior, no es palíndromo

def f(i,s): #ESTADO Q0
    s2 = s[:] #copia del stack
    if i==len(palabra): #si i es igual a la longitud de la palabra y no haz pop nada
        return False #no es palíndromo, estado de agregacion no es final
    # si una de las sig 3 lineas pasa, es palindromo
    res = False 
    res = res or d(i,s2) #transicion cuando pasamos al delete con E/E/E
    res = res or d(i+1,s2) #transicion cuando pasamos al delete con a/E/E o b/E/E
    s2.append(palabra[i]) #agrega la letra actual al stack, PT DE TRANSICION (lo q metes)
    res = res or f(i+1,s2) #transicion en la que te quedas en el mismo estado de agregaacion a/E/a o b/E/b
    return res #si no se cumple ninguna de las condiciones anteriores, no es palíndromo

print("El string",palabra,"es palíndromo?")
print(f(0,[]))