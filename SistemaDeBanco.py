import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_valor_positivo(mensagem):
    """Garante que o usuário digite um número válido e maior que zero."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print("Erro: O valor deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite apenas números (ex: 100.50).")


limpar_tela()
print("========================================")
print("       BEM-VINDO AO TRUSTBANK           ")
print("========================================")

senha_criada = input("Crie sua senha (somente números): ")
while not senha_criada.isdigit():
    senha_criada = input("Senha inválida. Digite apenas números: ")

print("\nSenha criada! Agora realize o acesso.")
while True:
    if input("Digite sua senha: ") == senha_criada:
        print("Acesso liberado.")
        break
    print("Senha incorreta. Tente novamente.")


saldo = 0.0
cheque_especial_total = 0.0
valor_utilizado_do_cheque = 0.0

primeiro_deposito = obter_valor_positivo("\nRealize seu primeiro depósito para abrir a conta: R$ ")
saldo += primeiro_deposito
cheque_especial_total = 50.0 if primeiro_deposito <= 500 else primeiro_deposito / 2
print(f"Conta aberta! Seu limite de cheque especial é: R$ {cheque_especial_total:.2f}")


def consultar_extrato():
    limite_disponivel = cheque_especial_total - valor_utilizado_do_cheque
    print("\n--- EXTRATO TRUSTBANK ---")
    print(f"Saldo Real em Conta: R$ {saldo:.2f}")
    print(f"Dívida no Cheque Especial: R$ {valor_utilizado_do_cheque:.2f}")
    print(f"Limite Disponível para Uso: R$ {limite_disponivel:.2f}")
    print("--------------------------")

def realizar_saque():
    global saldo, valor_utilizado_do_cheque
    valor = obter_valor_positivo("Valor do saque: R$ ")
    
    limite_atual_disponivel = cheque_especial_total - valor_utilizado_do_cheque
    capacidade_total = saldo + limite_atual_disponivel

    if valor <= saldo:
        saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    elif valor <= capacidade_total:
        valor_tirado_do_limite = valor - saldo
        saldo = 0
        valor_utilizado_do_cheque += valor_tirado_do_limite # ACUMULA a dívida corretamente
        print(f"Saque realizado! R$ {valor_tirado_do_limite:.2f} foram usados do seu limite.")
    else:
        print("Saldo e limite insuficientes para este valor.")

def realizar_deposito():
    global saldo, valor_utilizado_do_cheque
    valor = obter_valor_positivo("Valor do depósito: R$ ")
    
    if valor_utilizado_do_cheque > 0:
        taxa = valor * 0.20
        valor_apos_taxa = valor - taxa
        print(f"Aviso: Taxa de 20% aplicada pelo uso do limite (-R$ {taxa:.2f})")
        
        if valor_apos_taxa <= valor_utilizado_do_cheque:
            valor_utilizado_do_cheque -= valor_apos_taxa
            print(f"Depósito usado para abater a dívida. Dívida restante: R$ {valor_utilizado_do_cheque:.2f}")
        else:
            sobra = valor_apos_taxa - valor_utilizado_do_cheque
            valor_utilizado_do_cheque = 0
            saldo += sobra
            print("Dívida do cheque especial quitada! O restante foi para o seu saldo.")
    else:
        saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

def pagar_conta():
    global saldo, valor_utilizado_do_cheque
    valor = obter_valor_positivo("Valor do boleto/conta: R$ ")
    
    limite_atual_disponivel = cheque_especial_total - valor_utilizado_do_cheque
    
    if valor <= (saldo + limite_atual_disponivel):
        confirmar = input(f"Confirmar pagamento de R$ {valor:.2f}? (s/n): ").lower()
        if confirmar == 's':
            if valor <= saldo:
                saldo -= valor
            else:
                uso_limite = valor - saldo
                saldo = 0
                valor_utilizado_do_cheque += uso_limite
            print("Pagamento realizado com sucesso!")
        else:
            print("Operação cancelada.")
    else:
        print("Saldo insuficiente para pagar este boleto.")


while True:
    print("\n========== MENU TRUSTBANK ========")
    print("1 - Consultar Saldo/Extrato")
    print("2 - Realizar Saque")
    print("3 - Realizar Depósito")
    print("4 - Pagar Boleto")
    print("5 - Ver Limites")
    print("6 - Sair")
    print("===================================")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1": consultar_extrato()
    elif opcao == "2": realizar_saque()
    elif opcao == "3": realizar_deposito()
    elif opcao == "4": pagar_conta()
    elif opcao == "5": 
        print(f"\nLimite Total: R$ {cheque_especial_total:.2f}")
        print(f"Limite em Uso: R$ {valor_utilizado_do_cheque:.2f}")
    elif opcao == "6":
        print("Obrigado por utilizar o TrustBank. Até logo!")
        break
    else:
        print("Opção inválida.")