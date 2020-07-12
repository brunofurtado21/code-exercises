import pandas as pd, numpy as np,os

def get_input(type_of_variable,variable_name):

    #Só aceita números de um determinado tipo (int ou float)
    valid_type_of_variable = [int,float]
    if type_of_variable not in valid_type_of_variable:
        print ('Erro, tipo de variável inválido')
        exit()

    input_variable = input("Por favor, digite a {}: ".format(variable_name))

    #Tenta 5x conseguir um valor válido do usuário, caso contrário, fecha o programa
    for i in range(0,4):
        
        #Se for float, considerar ambos float e int, se for int, considerar só int
        try:
            input_variable = type_of_variable(input_variable)
        except:
            input_variable = input ("\nA {} precisa ser um número válido. \nPor favor, digite uma {} válida ".format(variable_name,variable_name))
            continue


        #Aqui só estamos lidando com variáveis maiores que 0
        if input_variable > 0:
            break

        else:
            input_variable = input ("\nA {} precisa ser maior que 0. \nPor favor, digite uma {} válida".format(variable_name,variable_name))
            continue

    #Se ao final das tentativas o usuário não inputar uma variável válida, fecha o programa
    try:
        input_variable = type_of_variable(input_variable)
        if input_variable <= 0:
            print("\nErro, por favor contactar o suporte técnico")
            exit()
        else:
            return input_variable
    except:
        print("\nErro, por favor contactar o suporte técnico")
        exit()



#Inputs do usuário

#Pede para o usuário inputar a idade atual
idade = get_input(int,'idade atual')
print ('\nSua idade atual é de: {} anos \n\n'.format(idade))

#Pede para o usuário inputar a idade atual
#Obs: no item, pedia para o nome da variável ser idade*, mas o python não aceita, portanto o nome ficou idade_final
idade_final = get_input(int,'idade de retirada do investimento')

if idade >= idade_final:
    print ('A idade de retirada precisa ser maior que sua idade atual.')
    idade_final = get_input(int,'idade de retirada do investimento')
    #Se o usuário inserir novamente uma idade de retirada menor do que a idade atual, fecha o programa
    if idade >= idade_final:
        print("Erro, por favor contactar o suporte técnico")
        exit()

print ('\nA idade final é de: {} anos \n\n'.format(idade_final))

#Pede para o usuário inputar a idade atual
quantia_final = get_input(float,'quantia final')
print ('\nA quantia final é de: {} \n\n'.format(quantia_final))

#Pede para o usuário inputar a idade atual
print ('Por favor, digite um número inteiro, ou separado por um ponto nas casas decimais, por exemplo: 0.12')
taxa_de_juros_anual = get_input(float,'taxa de juros anual')
print ('\nA taxa de juros anual é de: {} % ao ano \n\n'.format(taxa_de_juros_anual*100))





#Cálculo de quantia neecssária por mês:
"""Premissas:
    -Investimento ao início do ano, e retirada no final do ano
    -A taxa de juros anual incide desde o ano 0
    -Tempo de espera mínimo é de 1 ano."""

#Variaveis utilizadas no cálculo
diferenca_de_anos = idade_final - idade
taxa_de_juros_mensal = (taxa_de_juros_anual+1)**(1/12) - 1 #Considero os juros compostos no mês
diferenca_de_meses = diferenca_de_anos*12

#Aqui calculo iterativamente o rendimento das parcelas, a equação que define essa soma é: Somatório [ (1+i)^(n) ] sendo n de 1 até a diferença de anos
total_sum = 1*(1+taxa_de_juros_mensal)
for i in range(2,diferenca_de_meses+1):
    total_sum = total_sum + 1*(1+taxa_de_juros_mensal)**(i)

deposito_mensal = quantia_final/total_sum

deposito_mensal = round(deposito_mensal,2)

print ('Para chegar na quantia final de {} ao longo de {} anos,\nvocê precisa investir {} mensalmente.'
.format(quantia_final,diferenca_de_anos,deposito_mensal)
)






