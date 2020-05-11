import re, string
from os import system
from time import sleep 

def valorPagar():
    while True:
        valor = input("\nValor a pagar: ")
        
        if not re.match("[0-9]{2,20}(\.[0-9][0-9])?$", valor): 
            print("Erro! Valor inserido inválido!")
        else:
            return valor

###########################################################

def Data():
    while True:
        data = input("\nData de nascimento (DD-MM-AAAA): ")

        if not re.match("(0[1-9]|(1|2)[0-9]|3[0-1])\-(0[1-9]|1[0-2])\-(19[0-9]{2}|20[0-1][0-9])$", data): 
            print("Erro! Valor inserido inválido!")
        else:
            return data

###########################################################

def Nome():
    while True:
        nome = input("\nNome: ")
        
        if not re.match("[a-z]{3,15}( [a-z]{3,15}){0,7}$", nome): 
            print("Erro! Valor inserido inválido!")
        else:
            return nome

###########################################################

def NIF():
    nif = input('\nNIF: ')

    while True:
        nif = input("\nNIF: ")

        if not re.match("[0-9]{9}$", nif): 
            print("Erro! Valor inserido inválido!")
        else:
            return nif

###########################################################

def NIC():
    while True:
        nic = input("\nNIC: ")

        if not re.match("[0-9]{8,10}$", nic): 
            print("Erro! Valor inserido inválido!")
        else:
            return nic

###########################################################

def NCC():
    while True:
        ncc = input("\nNº do cartão de crédito: ")

        if not re.match("[0-9]{16}$", ncc): 
            print("Erro! Valor inserido inválido!")
        else:
            return ncc

###########################################################

def Data_CC():
    while True:
        data_CC = input("\nValidade do cartão de crédito (DD/MM): ")

        if not re.match("(0[1-9]|(1|2)[0-9]|3[0-1])\/(0[1-9]|1[0-2])$", data_CC) : 
            print("Erro! Valor inserido inválido!")
        else:
            return data_CC

###########################################################

def CVC():
    while True :
        cvc = input("\nCVC/CVV: ")

        if not re.match("[0-9]{3}$", cvc): 
            print("Erro! Valor inserido inválido!")
        else:
            return cvc

###########################################################

def main():
    valor=valorPagar()
    data=Data()
    nome=Nome()
    nif=NIF()
    nic=NIC()
    ncc=NCC()
    data_cc=Data_CC()
    cvc=CVC()
    
    system('clear')

    print('A validar dados, aguarde...')
    sleep(10)
    system('clear')

    print('\n###########################################################')
    print('\nValor a pagar: ' + valor)
    print('\nData de nascimento: ' + data)
    print('\nNome: ' + nome)
    print('\nNIF: ' + nif)
    print('\nNIC: ' + nic)
    print('\nNº do cartão de crédito: ' + ncc)
    print('\nValidade do cartão de crédito: ' + data_cc)
    print('\nCVC: ' + cvc)

    print('\n\t\tDados Validados!!')
    print('\n###########################################################')

main()