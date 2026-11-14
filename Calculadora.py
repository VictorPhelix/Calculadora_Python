print("Bem Vindo usuario a calculadora!")

while True:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))

    print("Escolha a operação desejada: ")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("5 - sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        resultado = n1 + n2
    elif opcao == "2":
        resultado = n1 - n2
    elif opcao == "3":
        resultado = n1 * n2
    elif opcao == "4":
        if n2 == 0:
            print("Não é possivel dividir por zero, tente novamente.")
            continue
        resultado = n1 / n2
    elif opcao == "5":
        print("saindo...")
        break
    else:
        print("opção Invalida, tente novamente.")
        continue

    print("Resultado é: ", resultado)
    continuar = input("Quer realizar outra operação? Sim ou Não?: ")
    if continuar == "Não":
        print("saindo...")
        break