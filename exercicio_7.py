import pandas as pd, numpy as np,os
import openpyxl
import xlsxwriter
import datetime
import warnings
warnings.filterwarnings("ignore")


#O programa permite inserir manualmente os dados de novos usuários na sheet "Novos Usuários",
#ou inputar manualmente todos os dados aqui.


#Aqui fica o caminho dos arquivos XLSX, a parte comentada é caso queira colocar em um local diferente do cwd.
cadastro_file_path = os.getcwd()+r'\Questao_7_Cadastro.xlsx'
bd_file_path = os.getcwd()+r'\Questao_7_BD.csv'
df_stats_file_path = os.getcwd()+r'\Questao_7_stats.xlsx'

#Cria uma lista de colunas, caso seja necessário criar os arquivos de Cadastro e/ou BD
standard_columns = ['DRE','Curso','Nome','Gênero','Data de Nascimento','Altura','Peso','CRA','Créditos Obtidos','Renda']

#Testa se os arquivos de cadastro e BD já existem no computador, se sim, ignora; se não, cria esses arquivos
if os.path.exists(cadastro_file_path):
    pass
else:
    df_columns = pd.DataFrame(columns=standard_columns)
    df_columns.to_excel(cadastro_file_path,index=False)

if os.path.exists(bd_file_path):
    pass
else:
    df_columns = pd.DataFrame(columns=standard_columns)
    df_columns.to_csv(bd_file_path,index=False)



#Primeiramente, le e adiciona os novos usuarios já adicionados na planilha, depois, pergunta se queremos adicionar manualmente,
#se sim, faz um append dos novos usuarios adicionados pela prompt no dataframe da worksheet, e salva ambos na sheet BD_Usuários.
novos_usuarios = pd.read_excel(cadastro_file_path,sheet_name = 'Novos Usuários')


#Conta quantos cadastros foram inputados no arquivo xlsx
total_cadastros = 2 + len(novos_usuarios)
final_range = 'A2:Z'+str(total_cadastros)


yes_or_no = input("\nDeseja inserir novos usuários? Digite 'sim' ou 'não'.")

while yes_or_no.upper() in ('SIM','YES',"'SIM'","'YES'"):
    data_list = []
    print ('***Atenção!***')
    print('\nLembre de botar datas no formato AAAA/MM/DD, e números fracionários separados por ponto.\n')
    #O usuário insere todos os dados necessários
    for column in novos_usuarios.columns:
        data = input("\nDigite o/a {}: ".format(column))
        data_list.append(data)
    data_df = pd.DataFrame(data_list).transpose()
    data_df.columns = novos_usuarios.columns
    novos_usuarios = novos_usuarios.append(data_df)
    yes_or_no = input("\nDeseja inserir mais usuários? Digite 'sim' ou 'não'.\n")


bd_usuarios = pd.read_csv(bd_file_path)
bd_usuarios = bd_usuarios.append(novos_usuarios)
bd_usuarios = bd_usuarios.reset_index(drop=True)

#Trata as datas do bd_usuarios
bd_usuarios['Data de Nascimento'] = bd_usuarios['Data de Nascimento'].apply(lambda x: (str(x)[:10]))
bd_usuarios['Data de Nascimento'] = bd_usuarios['Data de Nascimento'].apply(lambda x: x.replace('/','-'))
bd_usuarios['Data de Nascimento'] = bd_usuarios['Data de Nascimento'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d').date())

#Salva os dados de usuários na sheet BD
bd_usuarios.to_csv(bd_file_path,index=False)

#Deleta os cadastros do excel de Cadastro de novos usuários
workbook = openpyxl.load_workbook(cadastro_file_path)
worksheet = workbook.get_sheet_by_name('Novos Usuários')
# writer = pd.ExcelWriter(bd_file_path,engine='openpyxl')


#Itera anulando os valores da sheet
for row in worksheet[final_range]:
  for cell in row:
    cell.value = None

workbook.save(cadastro_file_path)
workbook.close()


#Converte o tipo de variável das colunas, para permitir analisá-las
for column in bd_usuarios.columns:
    column_type = (bd_usuarios[column].dtype)
    if column_type != 'float':
        try:
            bd_usuarios[column] = bd_usuarios[column].astype(float)
        except:
            # print ('Não foi possível converter o tipo da coluna {}'.format(column))
            pass


#Salva as informações descritivas sobre os alunos em um excel
df_describe = bd_usuarios.describe()
df_describe.to_excel(df_stats_file_path)


#Printa alguns dados interessantes sobre os alunos
cra_medio = round(bd_usuarios['CRA'].mean(),2)
cra_std = bd_usuarios['CRA'].std()

melhor_aluno = bd_usuarios[bd_usuarios['CRA'] == bd_usuarios['CRA'].max()]['Nome'].iloc[0]
cra_melhor_aluno = bd_usuarios['CRA'].max()

pior_aluno = bd_usuarios[bd_usuarios['CRA'] == bd_usuarios['CRA'].min()]['Nome'].iloc[0]
cra_pior_aluno = bd_usuarios['CRA'].min()

print('''\nO CRA médio dos seus alunos é de {} com um desvio padrão de {},
\nSeu melhor aluno é {} com um CRA de {},
\nSeu pior aluno é {} com um CRA de {}'''
.format(cra_medio,cra_std,
melhor_aluno,cra_melhor_aluno,
pior_aluno,cra_pior_aluno))


#Printa dados menos ligados a nota, e mais ligados ao perfil dos alunos
bd_grouped_genero = bd_usuarios.groupby(['Gênero']).count().reset_index()
bd_grouped_genero = bd_grouped_genero.sort_values(['Gênero'],ascending=False)
bd_grouped_genero = bd_grouped_genero[['Gênero','Altura']]
bd_grouped_genero.columns = ['Gênero','Count']

genero_mais_comum = bd_grouped_genero['Gênero'].iloc[0]

renda_media = bd_usuarios['Renda'].mean()

print('\nSeus alunos em maioria tem gênero {} e possuem renda média de {}'
.format(genero_mais_comum,renda_media))



print('\nPara mais dados sobre seus alunos, acesse o arquivo {}'
.format(df_stats_file_path))


