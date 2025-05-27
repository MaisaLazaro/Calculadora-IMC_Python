# Calculadora IMC

# Fórmulas:
# IMC= peso/altura2
# Classificação ICM = < 18.5- abaixo do peso; 18.5 a 24.9- peso normal; 25.0 a 29.9- sobrepeso; 30.0 ou mais- obesidade


while True:
    print("\nCálcule o IMC (Índice de Massa Corporal)")

    # Entrada de dados
    peso = float(input("Digite seu peso:"))
    h = float(input("Digite sua altura:"))

    # Cálculo de IMC
    imc = peso/h ** 2

    # Classificação do IMC
    if imc <= 18.5:
        classificacao = "Abaixo do peso"

    elif imc <= 24.9:
        classificacao = "Peso normal"

    elif imc <= 29.9:
        classificacao = "Sobrepeso"

    else:
        classificacao = "Obesidade"

    print(f"\nO valor do seu IMC é: {imc:.2f}")
    print(f"\nA classificação geral do IMC é: {classificacao}")

    repetir = input("\nDeseja calcular novamente? (s/n): ").strip().lower()
    if repetir != 's':
        print("Fim")
        break
