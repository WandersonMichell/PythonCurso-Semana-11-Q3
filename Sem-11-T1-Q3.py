# Função para ler números inteiros do usuário até que seja inserido um zero.
def ler_numeros():
    numeros = []

    while True:
        numero = int(input("Digite um número inteiro (0 para encerrar): ").strip())  # Solicita um número ao usuário

        if numero == 0:
            break

        if numero > 0:
            numeros.append(numero)  # Adiciona números positivos à lista
        else:
            print("Números negativos ou zero serão ignorados.")  # Informa ao usuário que números negativos ou zero são ignorados

    return numeros

# Função para encontrar o maior número na lista de números.
def encontrar_maior(numeros):
    if numeros:
        maior = max(numeros)  # Usa a função max para encontrar o maior número
        return maior
    return None

# Função para encontrar o menor número na lista de números.
def encontrar_menor(numeros):
    if numeros:
        menor = min(numeros)  # Usa a função min para encontrar o menor número
        return menor
    return None

def main():
    numeros = ler_numeros()  # Chama a função para ler números
    maior = encontrar_maior(numeros)  # Chama a função para encontrar o maior número
    menor = encontrar_menor(numeros)  # Chama a função para encontrar o menor número

    # Exibe o maior número, se houver algum na lista
    if maior:
        print(f"O maior número é: {maior}")
    else:
        print("Não foi inserido nenhum número positivo.")

    # Exibe o menor número, se houver algum na lista
    if menor:
        print(f"O menor número é: {menor}")
    else:
        print("Não foi inserido nenhum número positivo.")

if __name__ == "__main__":
    main()
