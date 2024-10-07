#função problema 1
def fibonacci(number: int):
    aux: int = 0
    previous: int = 0
    next: int = 1

    if(number == 1 or number == 0):
        return "\033[32mO numero pertence a sequencia\033[m"

    while next < number:
        aux = next
        next += previous
        previous = aux
        
    if( next > number):
        return "\033[31mO numero nao pertence a sequencia\033[m"

    return "\033[32mO numero pertence a sequencia\033[m"

#função problema 2
def quantidade_a(frase: str) -> int:
    return frase.upper().count("A")

#função problema 3
def soma():
    indice: int = 12
    soma:int = 0
    k:int = 1

    while k < indice:
        k += 1
        soma += k
    
    print(f"Soma = {soma}")

print(fibonacci(10)) # 1)
print(fibonacci(13)) # 1)
print(quantidade_a("Seja bem-vindo ao TargetTest")) # 2)
soma() # 3)