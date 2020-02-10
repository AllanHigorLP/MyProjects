def teste_primo(n):
    divisores = []
    for i in range(1,n+1):
        if (n%i==0):
            divisores.append(i)

    if(len(divisores)==2):
        return True
    else:
        return False


valido = False
while not valido:
    n = input("")
    if not n.isdigit():
        print("Digite um numero inteiro.")
    else:
        n = int(n)
        valido = True


soma = 0
for i in range(1,n+1):
    if(teste_primo(i)):
        soma += i
        
        
print("A soma dos numeros primos é "+str(soma))
