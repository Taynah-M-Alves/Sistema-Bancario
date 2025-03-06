# Sistema Bancário - Primeira Versão 🏦

## Objetivo Geral 🎯

Criar um sistema bancário com as operações: **sacar**, **depositar** e **visualizar extrato**.

## Desafio 🚀

Este projeto foi um **desafio proposto pelo Bootcamp da DIO (Digital Innovation One)** em parceria com a **Suzano**, com o objetivo de criar um sistema bancário simples utilizando **Python**.

Fomos contratados por um grande banco para desenvolver o seu novo sistema bancário. O banco deseja modernizar suas operações e escolheu a linguagem **Python** para essa tarefa. Para a primeira versão do sistema, as operações que devem ser implementadas são: **depósito**, **saque** e **extrato**.

## Requisitos do Sistema 📝

### 1. **Operação de Depósito 💰**
- O sistema deve permitir **deposições de valores positivos** na conta bancária.
- A versão 1 do sistema trabalha com **apenas 1 usuário**, logo, não é necessário preocupar-se com a identificação de agência ou número da conta bancária.
- O valor do depósito deve ser armazenado em uma variável e ser exibido na operação **extrato**.
- O sistema **não deve permitir depósitos de valores negativos**. ⚠️

### 2. **Operação de Saque 💳**
- O sistema deve permitir **3 saques diários** com um **limite máximo de R$ 500,00** por saque.
- Caso o usuário não tenha saldo suficiente, o sistema deve exibir uma mensagem informando que **não será possível sacar por falta de saldo**. 💸
- Todos os saques devem ser registrados e exibidos na operação **extrato**.

### 3. **Operação de Extrato 📊**
- A operação **extrato** deve listar todas as transações realizadas na conta, ou seja, **depósitos e saques**.
- No final da listagem, o sistema deve exibir o **saldo atual da conta**.
- Os valores devem ser exibidos no formato **R$ xxx.xx**, por exemplo: **R$ 1500.45**.

## Como Rodar o Projeto 🚀

### Pré-requisitos ⚙️

- **Python 3.x** instalado no seu computador.

### Passos 🔄


1. Clone este repositório:
    ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git

2.Navegue até o diretório do projeto:

    cd nome-do-repositorio

3.Execute o programa:

    python sistema_bancario.py

## Estrutura do Projeto 📁

- sistema_bancario.py: Arquivo principal com a implementação do sistema bancário.
- README.md: Documentação deste projeto.

## Funcionalidades ✨
- Depositar: O usuário pode depositar valores positivos na conta.
- Sacar: O usuário pode realizar até 3 saques diários, com limite de R$ 500,00 por saque, desde que tenha saldo suficiente.
- Extrato: O sistema exibe um histórico completo das transações e o saldo atual da conta.

## Exemplos de Uso 💡

### Depósito:
Digite o valor a ser depositado: 1000 </br>
Deposito realizado com sucesso! Seu saldo atual é 1000.

### Saque:
Digite o valor a ser sacado: 200 </br>
Saque realizado com sucesso! Seu saldo atual é 200.

### Extrato:
=============== Extrato ================

+R$4000.00  
-R$200.00  

<br>

saldo final: R$3800.00

=======================================



## Contribuições 🤝
Contribuições são bem-vindas! Se você deseja melhorar o sistema bancário v1, sinta-se à vontade para criar um fork deste repositório, adicionar suas melhorias e abrir um pull request.

## Licença 📄
Este projeto está licenciado sob a MIT License.
