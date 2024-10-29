#variaveis
saida = ''

#funçoes
def adicao (num1,num2):
    return num1+num2
def subtracao (num1,num2):
    return num1-num2
def multiplicacao (num1,num2):
    return num1*num2
def divisao (num1,num2):
    if num2!=0:
        return num1/num2
    else:
        return "Nao foi possivel realizar a divisao por 0"

#funcao calculadora
def calculadora (num1,num2,operacao):
    if operacao == "+" or operacao == "adicao":
        return adicao(num1,num2)
    elif operacao == "-" or operacao == "subtracao":
        return subtracao(num1,num2)
    elif operacao == "*" or operacao == "multiplicacao":
        return multiplicacao(num1,num2)
    elif operacao == "/" or divisao == "divisao":
        return divisao(num1,num2)
    else:
        return "Não há calculos a resolver"

while saida.lower() != "n":
    try:
        num1=float(input("Digite o numero"))
        num2=float(input("Digite o segundo numero"))
        operacao=input("Digite a operação desejada +,-,*, / ou nome da operacao")
        resultado=calculadora (num1,num2,operacao)
        print(f"Aqui esta o resultado da sua operação {resultado}")
        saida=input("Deseja continuar as operacoes? S para sim ou N para nao: \n")
    except:
        print("Operacao invalida")

print("Operacao finalizada")

