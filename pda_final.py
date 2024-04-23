
# Estado q1: Elimina las letras de la pila y verifica si la palabra es palindromo (si la pila esta vacia y el indice llega al final de la palabra)
def is_palindrome(palabra):

    def q1(i, stack):
        stack2 = stack[:] # Copia la pila para no modificar la original
        print(f"Indice actual: {i}, Pila actual: {stack2}") # Imprime el indice y la pila actual 
    
        # Si el indice llega al final de la palabra y la pila esta vacia, regresa True (es palindromo)
        if i == len(palabra) and len(stack2) == 0:
            return True
        # Si el indice llega al final de la palabra pero la pila no esta vacia, regresa False 
        if i >= len(palabra):
            return False
        # Si la pila no esta vacia y el tope de la pila coincide con el caracter en el indice i, elimina el tope de la pila y continua verificando
        if stack2 and (stack2[-1] == palabra[i]):
            stack2.pop()
            return q1(i + 1, stack2)
        # Si no, regresa False (no es palindromo)
        return False


    # Estado q0: Añade las letras a la pila o ignora un caracter (en caso de ser impar)

    def q0(i, stack):
        stack2 = stack[:]  # Copia la pila para evitar modificar la original
            
        if i == len(palabra): # Si el indice llega al final de la palabra, regresa False (no es palindromo)
            return False
        
        # Si cumple con las transiciones de q0 y q1, regresa True (es palindromo)
        res = False # Inicializa la variable de resultado (el estado final) en False
        # Checa si la letra actual a partir del indice i es un palindromo con la pila actual
        res = res or q1(i, stack2)
        # Checa si la siguiente letra en la palabra forma un palindromo con la pila actual
        res = res or q1(i + 1, stack2)
        # Añade la letra actual a la pila y checa si la palabra resultante es un palindromo
        stack2.append(palabra[i])
        res = res or q0(i + 1, stack2)
        # Regresa el resultado final
        return res
    
    return q0(0, []) # Regresa el resultado de la funcion q1


def test_palindrome():
    print("Test 1: abba")
    test = is_palindrome("abba")
    print(f"Es palindromo: {test}\n")

    print("Test 2: aba")
    is_palindrome("aba")
    test = print(f"Resultado: {test}\n")

    print("Test 3: bbabb")
    test = is_palindrome("bbabb")
    print(f"Es palindromo: {test}\n")

    print("Test 4: bbab")
    test = is_palindrome("bbab")
    print(f"Es palindromo: {test}\n")

    print("Test 5: anitalavalatina")
    test = is_palindrome("anitalavalatina")
    print(f"Es palindromo: {test}\n")

    print("Test 6: racecar")
    test = is_palindrome("racecar")
    print(f"Es palindromo: {test}\n")

    print("Test 7: a")
    test = is_palindrome("a")
    print(f"Es palindromo: {test}\n")


if __name__ == "__main__":
    test_palindrome()
