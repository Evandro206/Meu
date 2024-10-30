class Conta:
    def __init__(self,numero,tipo,saldo):
        self.numero = numero
    @staticmethod
    def teste():    
        tipo_de_conta = ['corrente','poupanca']
        while True:
            while True:
                tipo = input("Digite o tipo de conta que deseja (corrente/poupanca): ").lower()
                if tipo in tipo_de_conta:
                    break
                else:
                    print("Tipo de conta digitado incorretamente, tente novamente")
            break
        print(tipo)
        print(tipo)
        print(tipo)
        print(tipo)
        print(tipo)
        print(tipo)
Conta.teste()
