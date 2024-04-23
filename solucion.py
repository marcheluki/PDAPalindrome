palabra = "abbba"

def d(i, s):
    s2 = s[:]
    print(i,s2)
    if i == len(palabra) and len(s2)==0:
        return True
    if i >= len(palabra):
        return False
    if s2 and (s2[-1] == palabra[i]):
        s2.pop()
        return d(i+1,s2)
    return False

def f(i,s):
    s2 = s[:]
    if i==len(palabra):
        return False
    res = False
    res = res or d(i,s2)
    res = res or d(i+1,s2)
    s2.append(palabra[i])
    res = res or f(i+1,s2)
    return res

print(f(0,[]))