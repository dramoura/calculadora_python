def calcular_idade(ano_atual, ano_nascimento):
    idade = ano_atual - ano_nascimento
    return idade

while True:
     idade = ano_atual - ano_nascimento
     nome = input("Digite seu nome completo: ")
     ano_nascimento = int(input("Digite seu ano de nascimento (1922-2021): "))
     ano_atual = int(input("Digite o ano em que estamos: "))

     if 1922 <= ano_nascimento <= 2021:
        print(nome)
        print(idade)
        break
     
     else:
         print("Ano errado, por favor, tente novamente.")   