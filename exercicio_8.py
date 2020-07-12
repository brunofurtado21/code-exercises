import pandas as pd, numpy as np,random
import concurrent.futures
import time


#Variáveis iniciais
range_n = [10**5,10**7,10**9]
range_k = [1,2,4,8,16]
start = -50
stop = 50

#Cria um dataframe para armazenar os dados a serem plotados
df_dados = pd.DataFrame(columns=['N','K','Tempo'])

def multithread_sum(n,k,start,stop):

    #Define o vetor base utilizado os parâmetros dados do problema e a biblioteca random.choices
    base_range = range(start,stop,1)

    #Esse é o vetor que iremos somar
    vetor_base = random.choices(base_range,k=n)

    #Define o tamanho das 'partes' iguais a serem somadas, e qual o resto a ser adicionado na última parte, caso não seja uma divisão perfeita
    chunk_size = n//k
    extra_values = n%k
    
    #Aqui está o vetor onde iremos associar cada sublista a um thread
    chunked_vetor_base = chunks(vetor_base,k,extra_values)

    #Aqui armazenaremos os resultados das sublistas
    vetor_sum = []

    #Mede quantos chunks existem, pois no caso de haverem k-1 (divisão sem resto de n/k), não podemos iterar até k
    chunked_length = len(chunked_vetor_base)


    #Começa a contar o tempo que a função levará para executar
    start_time = time.time()

    #Utiliza a biblioteca concurrent.futures para realizar as somas simultâneas
    with concurrent.futures.ThreadPoolExecutor(max_workers=k) as executor:
        #Cria as funções em paralelo de forma iterativa
        for threads in range(0,chunked_length):
            vetor_parcial = chunked_vetor_base[threads]
            executor.submit(append_sum,vetor_parcial,vetor_sum)
            # append_sum(vetor_parcial,vetor_sum)

    end_time = time.time()
    return end_time - start_time


#Faz uma lista de listas, para dividir quais partes iremos somar paralelamente do nosso vetor_base
def chunks(list, k, append_last):
    chunked_list = []
    #Yield successive k-sized chunks from list
    for chunk_parts in range(0, len(list), k):
        chunked_list.append(list[chunk_parts:chunk_parts + k])
        # print (chunked_list)
    
    #Se não for uma divisão perfeita, integra a última lista na penúltima, para não ultrapassar k threads
    if append_last > 0:
        last_list = chunked_list[-1:][0]
        length = len(last_list)
        for j in range(0,length):
            item_to_append = last_list[j]
            chunked_list[-2:-1][0].append(item_to_append)

        chunked_list = chunked_list[:-1]
        # print (chunked_list)
    return chunked_list


#Função simples que appenda na lista o valor das somass
def append_sum(vetor_parcial,vetor_sum):
    soma = sum(vetor_parcial)
    vetor_sum.append(soma)


#Armazena no DF de dados, o tempo,n e k utilizados em cada iteração
print ('Para os números originais da função, demora muito para executar')
for n in range_n:
    for k in range_k:
        print ('Iterando para n = {} e k = {}'.format(n,k))
        tempo = multithread_sum(n,k,start,stop)
        lista_dados = [n,k,tempo]
        df_dados.loc[len(df_dados)] = lista_dados


#Para cada N, plota o tempo em função de K
for n in range_n:
    df_dados_n_especifico = df_dados[df_dados['N'] == n].copy()
    df_dados_n_especifico.plot.scatter(x='Tempo',y='K',title="N = " +str(n))


