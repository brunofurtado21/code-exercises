# Exercicios


## Questão 5

Implementação dos algoritmos Merge Sort e Bubble Sort, em um range de 'n' números, que podem ter valores entre 'start' e 'stop'.
Todos esses 3 parâmetros são definidos pelo usuário


## Questão 6

Utiliza como base a função get_input, para pegar os valores de idade atual, idade* que chamei de idade final e taxa de juros da aplicação.

As seguintes premissas são utilizadas no cálculo da função:
    - Investimento ao início do ano, e retirada no final do ano
    - A taxa de juros anual incide desde o ano 0
    - Tempo de espera mínimo é de 1 ano.

Fora isso, é um cálculo bem simples e iterativo.

Primeiramente, divide a diferença de anos em 12 partes, para achar o número de meses onde haverá aporte financeiro

Depois, calcula do último até o primeiro mês de investimento, quanto cada mês irá render ao longo dos anos investidos, usando a taxa de juros fornecida, convertida para mensal (considerando que são juros compostos)

Por fim, divide o valor alvo pela soma dos rendimentos dos meses, achando então o valor unitário a ser investido todo mês.


## Questão 7

Permite que o usuário cadastre dados de vários alunos, que podem ou ser inputados em um excel, ou serem adicionados manualmente no terminal durante a execução.

Ao executar, ele checa se o usuário possui os arquivos de inscrição diretamente no xlsx, e o BD em csv. O BD fiz em csv e não xlsx, pois o csv consome menos memória, assim fica possível fazer um BD maior.

Depois de o usuário inputar (ou nao) novos alunos, exibe alguns dados voltados para as notas dos alunos, e também sobre o perfil dos alunos, como gênero mais frenquente (não mostrei percentual caso exista algum 'não declarado' ou algo do tipo), renda média e desvio padrão da renda dos alunos.

Por fim, salva um xlsx com alguns dados adicionais das colunas que possuem valor numérico em um xlsx, utilizando a função .describe() do pandas.


## Questão 8

OBS: Uma das desvantagens do multithread no Python é que devido ao GIL (Global Interpreter Lock) apenas uma thread pode executar código Python ao mesmo tempo. O resultado disso é que multithreading no Python ainda otimiza consumos de recursos externos (pois enquanto uma thread espera o recurso externo outra pode ser executada) porém não existem ganhos de performance para programas como esse, que necessitam de processamento paralelo, inclusive, o programa em questão chega a executar mais rápido quando não são utilizados multithreads, devido ao custo de processamento de criar e manter os threads.
Já implementei uma solução de multithreading na Ton, onde eu acessava diversos bancos de dados, então ao invés de esperar a execução das queries uma após a outra, o programa mandava a requisição para os bancos, e aguardava a resposta em paralelo, consumindo cerca de 1/4 do tempo original de execução do programa. 


Sobre o exercício:
O programa gera vetores de números aleatórios com reposição, de tamanho 'N' e seus números variando do start até o stop. Depois, divide esse vetor de tamanho N em K partes, sendo a última maior caso N/K não seja uma divisão perfeita. Depois, calculo o tempo total de execução do código para N ; K, utilizando K threads paralelos, e armazeno os valores de N, K e o tempo de execução em um dataframe, que é plotado depois.

Como já citei acima, achei estranho o programa rodar mais rápido quanto maior o K, dadas as limitações de multithreading no python. Ao investigar, percebi que mesmo utilizando um único thread, o programa rodava mais rápido ao calcular K listas de um tamanho N / K ao invés de uma lista de tamanho N. Portanto, o ganho não era do multithread e sim referente a forma como a função built-in sum() do python é implementada.

Além disso, consegui testar a lógica e perceber que de fato está funcionando, para valores menores dos que os pedidos no exercício. Com N de um tamanho até 10**6, o tempo de execução é razoável, porém após alguns testes, percebi que o tempo de execução aparenta escalar linearmente de acordo com o tamanho de N e escala em função de 1/K em relação ao tamanho de K.
No meu computador, demorou cerca de 1.6 segundos para N = 10^5 com K = 1, aproximadamente 0.8 segundos para N = 10^5 e K = 2, 160 segundos para N = 10^7 e K = 1, etc.
Sendo assim, tomando como base o 1.6 segundos para N = 10^5 e K = 1, o tempo estimado para o código inteiro rodando de N em (10^5,10^7,10^9) e K em (1,2,4,8,16), seria um total de aproximadamente 31313 segundos (521 minutos ou 8.7 horas)


