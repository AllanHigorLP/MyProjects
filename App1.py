def int_rom(n):
    if(0< n <3999):
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []

    for i in range(len(ints)):
        count = int(n / ints[i])
        result.append(nums[i] * count)
        n -= ints[i] * count
    return ''.join(result)  





valido = False
while not valido:
    ano = input("")
    
    if not ano.isdigit():
        print("Por favor, digite um ano entre 1 e 9999.")
    elif(len(ano))>4 or int(ano)==0:
        print("Por favor, digite um ano entre 1 e 9999.")
    else:
        valido = True


sec = 0
tam_ano = len(ano)


if(tam_ano <= 2):
    sec = 1
elif(tam_ano <=3):
    sec = int(ano[0]) + 1
else: 
    sec = int(ano[0])*10 + int(ano[1]) + 1

print("O ano "+ano+" faz parte do século "+str(int_rom(sec)))

