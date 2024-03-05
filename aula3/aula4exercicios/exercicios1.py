def operacoes_matematicas(numero1, numero2):

    soma = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    
    if numero2 != 0:
        divisao = numero1 / numero2
    else:
        divisao = "Divisão por zero não é permitida"

    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacoes_matematicas(numero1, numero2)
