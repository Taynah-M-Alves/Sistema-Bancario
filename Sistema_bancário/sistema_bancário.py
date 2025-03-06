menu = """
Operações disponiveís

[a]Depositar
[b]Sacar
[c]Ver o extrato
[d]Finalizar atendimento

Escreva a letra correspondente a operação que você deseja executar:
"""
    
extrato = "" #lista responsavel por armazenar o histórico de transações do cliente.
saldo = 0 
limite_saque_diario = 0
limite_valor_por_saque= 500
saque_diario = 0

# Essa funcao é responsavel por: 
# depositar(adiciona o valor_deposito do saldo);
#  salvar o valor_deposito no extrato;
# retornar uma mensagem que o deposito foi realizado.
def depositar(valor_deposito):
        global saldo
        global extrato
        saldo += valor_deposito
        extrato += f"+ R${valor_deposito:.2f}\n" # adiciona o valor depositado a lista extrato
        return print(f"Deposito realizado com sucesso! Seu saldo atual é {saldo}.")

# Essa funcao é responsavel por: 
# sacar(debitar o valor_saque do saldo); 
#  salvar o valor_saque no extrato;
# retornar uma mensagem que o saque foi realizado.
def sacar(valor_saque):
        global saldo
        global extrato
        global saque_diario
        saldo -= valor_saque
        extrato += f"- R${valor_saque:.2f}\n" # adiciona o valor sacado a lista extrato
        saque_diario += 1
        return print(f"Saque realizado com sucesso! Seu saldo atual é {saldo}.")

# a funcao while garante que o ciclo será repetido ate que o usuario digite "d"
while True:

    #Variavel responsavél por armazenar a resposta digitada pelo cliente
    resposta = input(menu)

    #Variavel responsavel por transformar a resposta da cliente em letra minuscula para não dar erro na estrutura condicional.
    operacao = resposta.lower()

    if operacao == "a":
            valor_deposito = float(input("escreva o valor que deseja depositar:"))
            if valor_deposito > 0:
                depositar(valor_deposito)
            else:
                print("Não foi possível realizar esse depósito! O valor informado é incorreto.")    
        

    elif operacao == "b": 
            
            valor_saque = float(input("escreva o valor que deseja sacar:"))

            excedeu_limite_saldo = valor_saque > saldo

            excedeu_limite_valor = valor_saque > limite_valor_por_saque

            excedeu_limite_saque_diario = saque_diario >= 3 


            saque_diario = 0

            #Opção executada quando o valor de saque é maior do que o saldo disponivel
            if excedeu_limite_saldo:
                print("Saldo insuficiente.")
                print("Não foi possível realizar o saque.")
                        

            #opção executada quando o valor de saque é maior do que R$500.00(limite de saque)
            elif excedeu_limite_valor:
                print("Não foi possível realizar o saque! Seu limite máximo por saque é R$500.00.")
                print("Se necessário tente dividir o valor em vários valores abaixo de R$500.00.")
                        

            #opção executada quando o limite de saque diario é atingido
            elif excedeu_limite_saque_diario:
                print("O limite de saque diário já foi atingido, volte amanhã para sacar novamente.")
                        

            #opção executada quando o saldo é suficiente para o saque e o limite diario de saque não foi atingido
            elif valor_saque > 0:
                sacar(valor_saque)

                    
                    
            #Opção executada caso o usuario digite um numero invalido tipo -200
            else:
                print("Operação falhou! O valor informado é inválido")
            

    #Opção executada quando o usuário quer visualizar o extrato e saldo final        
    elif operacao == "c":
        print(f"================Extrato================", end="\n \n")
        print("Não foram realizadas movimentações.\n" if not extrato else extrato)
        print(f"saldo final: R${saldo:.2f}")
        print("=======================================")
    
    #opção executada quando o usuário quer finalizar o seu atendimento
    elif operacao == "d":
        print("Atendimento finalizado. Obrigado pela preferência!")
        break

    #Opção executada quando o usuario coloca alguma resposta diferente de "a","b","c","d"
    else:
        print("Resposta incorreta, digite a letra correspondente ao serviço que deseja:")
        
    

