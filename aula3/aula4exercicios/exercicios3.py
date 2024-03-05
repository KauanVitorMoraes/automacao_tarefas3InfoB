def calcular_operacao(numero1, numero2, operador):
    if operador == '+':
        resultado = numero1 + numero2
    elif operador == '-':
        resultado = numero1 - numero2
    elif operador == '*':
        resultado = numero1 * numero2
    elif operador == '/':
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return "Divisão por zero não é permitida"
    else:
        return "Operador inválido"
    
    return resultado


def formatar_saida(resultado, operador):
    return f"O resultado da {operador} é {resultado}"

def main():
    while True:
        
        entrada = input("Digite dois números reais e um operador matemático (por exemplo, '1 2 +'): ")
        numeros, operador = entrada.split()[:2], entrada.split()[2]

        numero1, numero2 = float(numeros[0]), float(numeros[1])

        resultado = calcular_operacao(numero1, numero2, operador)

        print(formatar_saida(resultado, operador))

        continuar = input("Deseja continuar? (S para Sim, N para Não): ").upper()
        if continuar != 'S':
            break

if __name__ == "__main__":
    main()
