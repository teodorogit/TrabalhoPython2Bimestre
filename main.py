import os

def clear_terminal():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')

class Cliente:
    codigo_atual = 1
    
    def __init__(self, nome):
        self.nome = nome
        self.codigo = Cliente.codigo_atual
        Cliente.codigo_atual += 1

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}"

# BANCO DE DADOS FAKE
banco_clientes = []


def inicio_sistema():
    print("---- SISTEMA DE AGENDAMENTO DE CLIENTE ----")
    print()
    opc = input('ACOES DISPONIVEIS -> \n1- AGENDAR CLIENTE \n2- VER HORÁRIOS AGENDADOS \n3- CANCELAR HORÁRIO \nESCOLHA UMA AÇÃO: ')
    
    # Verificar se a opção é válida
    while opc not in ["1", "2", "3"]:
        print("Digite uma opção válida.")
        opc = input('ACOES DISPONIVEIS \n1- AGENDAR CLIENTE \n2- VER HORÁRIOS AGENDADOS \n3- CANCELAR HORÁRIO \nESCOLHA UMA AÇÃO: ')
    
    if opc == "1":
        clear_terminal()
        print("AGENDAR CLIENTE")
        nome = input('Digite o nome do cliente: ')
        c1 = Cliente(nome)
        banco_clientes.append(c1)
        print()
        print(f"Cliente {c1.nome} foi agendado com sucesso.")
        print()

  
    elif opc == "2":
        clear_terminal()
        print('LISTA DE  CLIENTES AGENDADOS:')
        if banco_clientes:
            for  cliente in banco_clientes:
                print()
                print(f"> {cliente}")
                print()

        else:
            print("Nenhum cliente agendado.")

    elif opc == "3":
        print('CANCELAR HORÁRIO')
        if banco_clientes:
            for index, cliente in enumerate(banco_clientes):
                print(f"{index} - {cliente}")
            escolha = int(input("Escolha o número do cliente para cancelar o agendamento: "))
            if 0 <= escolha < len(banco_clientes):
                cliente_removido = banco_clientes.pop(escolha)
                print(f"Agendamento do cliente {cliente_removido.nome} cancelado.")
            else:
                print("Escolha inválida.")
        else:
            print("Nenhum cliente agendado para cancelar.")
    
  

while True:
    inicio_sistema()
