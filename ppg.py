# PPG - Bianca NUnes Coelho
# ctrl + alt + i

# Bibliotecas necessárias
import numpy as np
import csv
import os
import pandas as pd
import requests

# Menu principal
def mensagem_principal():
    print('Bem vindo ao sistema de classificação automátic de alunos do PPG!')
    print('Escolha uma das opções abaixo:')
    print('1 - Ler arquivo csv')
    print('2 - Listar todos os alunos inscritos')
    print('3 - Classificar alunos no Mestrado')
    print('4 - Classificar alunos no Doutorado')
    print('5 - Sair')

# Submenus
def menu2():
    print("1 - Listar alunos inscritos no Mestrado")
    print("2 - Classsificação: passar para csv")
    print("3 - Sair")

def menu3():
    print("1 - Listar alunos inscritos no Doutorado")
    print("2 - Classsificação: passar para csv")
    print("3 - Sair")

# Função para ler o arquivo csv e transformá-lo em um dataframe com pandas
def le_arquivo():
    nome_arquivo = input()
    nome_arquivo = nome_arquivo + '.csv'
    if os.path.exists(nome_arquivo):
        print('Arquivo encontrado!')
        # Lê o arquivo csv e retorna um DataFrame
        df = pd.read_csv(nome_arquivo)
        return df
    else:
        print('Arquivo não encontrado!')
        return None

# Classe ALUNO

class Aluno:
    def __init__(self, nome_completo, data_nascimento, email, nome_mae, cpf, identidade, data_emissao_identidade, orgao_emissor_identidade, numero_titulo_eleitoral, numero_serie_documento_militar, endereco_residencial, cidade_residencia, estado_residencia, telefone_contato, link_curriculo_lattes, reservas_vagas, numero_siape, nome_curso, tipo_curso, instituicao, ano_conclusao, nome_curso_anterior, tipo_curso_anterior, instituicao_anterior, ano_conclusao_anterior, local_trabalho, atuacao, ingles_leitura, ingles_escrita, ingles_fala, tipo_inscricao, semestre_ingresso, orientador_preferencial, segunda_opcao, terceira_opcao, dedicacao_integral, vinculo_empregaticio, interesse_bolsa, arquivo_projeto_doutorado, titulo_publicacao1, local_publicacao1, tipo_publicacao1, qualis_publicacao1, comprovacao_publicacao1, primeiro_autor1, titulo_publicacao2, local_publicacao2, tipo_publicacao2, qualis_publicacao2, comprovacao_publicacao2, primeiro_autor2, titulo_publicacao3, local_publicacao3, tipo_publicacao3, qualis_publicacao3, comprovacao_publicacao3, primeiro_autor3, titulo_publicacao4, local_publicacao4, tipo_publicacao4, qualis_publicacao4, comprovacao_publicacao4, primeiro_autor4, titulo_publicacao5, local_publicacao5, tipo_publicacao5, qualis_publicacao5, comprovacao_publicacao5, primeiro_autor5, curriculo_lattes, diploma_graduacao, diploma_mestrado, historico_graduacao, historico_mestrado, identidade_doc, cpf_doc, titulo_eleitor, certificado_militar, certidao_casamento, comprovante_pagamento, documentacao_adicional, outro_documento, id_usuario, timestamp, last_updated, created_by, updated_by, draft, ip, id, key):    
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.email = email
        self.nome_mae = nome_mae
        self.cpf = cpf
        self.identidade = identidade
        self.data_emissao_identidade = data_emissao_identidade
        self.orgao_emissor_identidade = orgao_emissor_identidade
        self.numero_titulo_eleitoral = numero_titulo_eleitoral
        self.numero_serie_documento_militar = numero_serie_documento_militar
        self.endereco_residencial = endereco_residencial
        self.cidade_residencia = cidade_residencia
        self.estado_residencia = estado_residencia
        self.telefone_contato = telefone_contato
        self.link_curriculo_lattes = link_curriculo_lattes
        self.reservas_vagas = reservas_vagas
        self.numero_siape = numero_siape
        self.nome_curso = nome_curso
        self.tipo_curso = tipo_curso
        self.instituicao = instituicao
        self.ano_conclusao = ano_conclusao
        self.nome_curso_anterior = nome_curso_anterior
        self.tipo_curso_anterior = tipo_curso_anterior
        self.instituicao_anterior = instituicao_anterior
        self.ano_conclusao_anterior = ano_conclusao_anterior
        self.local_trabalho = local_trabalho
        self.atuacao = atuacao
        self.ingles_leitura = ingles_leitura
        self.ingles_escrita = ingles_escrita
        self.ingles_fala = ingles_fala
        self.tipo_inscricao = tipo_inscricao
        self.semestre_ingresso = semestre_ingresso
        self.orientador_preferencial = orientador_preferencial
        self.segunda_opcao = segunda_opcao
        self.terceira_opcao = terceira_opcao
        self.dedicacao_integral = dedicacao_integral
        self.vinculo_empregaticio = vinculo_empregaticio
        self.interesse_bolsa = interesse_bolsa
        self.arquivo_projeto_doutorado = arquivo_projeto_doutorado
        self.titulo_publicacao1 = titulo_publicacao1
        self.local_publicacao1 = local_publicacao1
        self.tipo_publicacao1 = tipo_publicacao1
        self.qualis_publicacao1 = qualis_publicacao1
        self.comprovacao_publicacao1 = comprovacao_publicacao1
        self.primeiro_autor1 = primeiro_autor1
        self.titulo_publicacao2 = titulo_publicacao2
        self.local_publicacao2 = local_publicacao2
        self.tipo_publicacao2 = tipo_publicacao2
        self.qualis_publicacao2 = qualis_publicacao2
        self.comprovacao_publicacao2 = comprovacao_publicacao2
        self.primeiro_autor2 = primeiro_autor2
        self.titulo_publicacao3 = titulo_publicacao3
        self.local_publicacao3 = local_publicacao3
        self.tipo_publicacao3 = tipo_publicacao3
        self.qualis_publicacao3 = qualis_publicacao3
        self.comprovacao_publicacao3 = comprovacao_publicacao3
        self.primeiro_autor3 = primeiro_autor3
        self.titulo_publicacao4 = titulo_publicacao4
        self.local_publicacao4 = local_publicacao4
        self.tipo_publicacao4 = tipo_publicacao4
        self.qualis_publicacao4 = qualis_publicacao4
        self.comprovacao_publicacao4 = comprovacao_publicacao4
        self.primeiro_autor4 = primeiro_autor4
        self.titulo_publicacao5 = titulo_publicacao5
        self.local_publicacao5 = local_publicacao5
        self.tipo_publicacao5 = tipo_publicacao5
        self.qualis_publicacao5 = qualis_publicacao5
        self.comprovacao_publicacao5 = comprovacao_publicacao5
        self.primeiro_autor5 = primeiro_autor5
        self.curriculo_lattes = curriculo_lattes
        self.diploma_graduacao = diploma_graduacao
        self.diploma_mestrado = diploma_mestrado
        self.historico_graduacao = historico_graduacao
        self.historico_mestrado = historico_mestrado
        self.identidade_doc = identidade_doc
        self.cpf_doc = cpf_doc
        self.titulo_eleitor = titulo_eleitor
        self.certificado_militar = certificado_militar
        self.certidao_casamento = certidao_casamento
        self.comprovante_pagamento = comprovante_pagamento
        self.documentacao_adicional = documentacao_adicional
        self.outro_documento = outro_documento
        self.id_usuario = id_usuario
        self.timestamp = timestamp
        self.last_updated = last_updated
        self.created_by = created_by
        self.updated_by = updated_by
        self.draft = draft
        self.ip = ip
        self.id = id
        self.key = key

        self.pontuacao_publicacao1 = 0
        self.pontuacao_publicacao2 = 0
        self.pontuacao_publicacao3 = 0
        self.pontuacao_publicacao4 = 0
        self.pontuacao_publicacao5 = 0
        self.nota_geral_publicacoes = 0
        self.nota_historico = 0
        self.media_graduacao = 0
        self.nota_final = 0

    # calcula pontuação das publicações
    def calcular_pontuacao(self):
        qualis_pontuacao = {
            'A1': 5.00, 'A2': 4.38, 'A3': 3.75, 'A4': 3.13,
            'B1': 2.50, 'B2': 1.00, 'B3': 0.50, 'B4': 0.25,
            'sem qualis': 0.20
        }
        coautor_multiplicador = {
            'A1': 1.67, 'A2': 1.46, 'A3': 1.25, 'A4': 1.00,
            'B1': 0.83, 'B2': 0.33, 'B3': 0.17, 'B4': 0.08,
            'sem qualis': 0.06
        }

        def pontuacao_individual(qualis, primeiro_autor):
            if qualis in qualis_pontuacao:
                if primeiro_autor == 'Sim':
                    return qualis_pontuacao[qualis]
                else:
                    return coautor_multiplicador[qualis]
            return 0

        publicacoes = [
            (self.qualis_publicacao1, self.primeiro_autor1),
            (self.qualis_publicacao2, self.primeiro_autor2),
            (self.qualis_publicacao3, self.primeiro_autor3),
            (self.qualis_publicacao4, self.primeiro_autor4),
            (self.qualis_publicacao5, self.primeiro_autor5)
        ]

        if self.tipo_inscricao.lower() == 'mestrado':
            publicacoes = publicacoes[:3]
        elif self.tipo_inscricao.lower() == 'doutorado':
            publicacoes = publicacoes[:5]

        self.pontuacao_publicacao1 = pontuacao_individual(*publicacoes[0])
        self.pontuacao_publicacao2 = pontuacao_individual(*publicacoes[1])
        self.pontuacao_publicacao3 = pontuacao_individual(*publicacoes[2])
        
        if len(publicacoes) > 3:
            self.pontuacao_publicacao4 = pontuacao_individual(*publicacoes[3])
            self.pontuacao_publicacao5 = pontuacao_individual(*publicacoes[4])

        self.nota_geral_publicacoes = sum([
            self.pontuacao_publicacao1,
            self.pontuacao_publicacao2,
            self.pontuacao_publicacao3,
            self.pontuacao_publicacao4,
            self.pontuacao_publicacao5
        ])

        # Calculo da pontuação histórico de graduação
        if self.tipo_curso.lower() == 'bacharelado' or self.tipo_curso.lower() == 'licenciatura':
            if self.media_graduacao == 5 or self.media_graduacao < 5:
                self.nota_historico = 0
            elif self.media_graduacao > 5:
                self.nota_historico = self.media_graduacao - 5
        else:
            self.nota_historico = 2

    # calcula nota final
    def calcula_nota_final(self):

        if self.tipo_inscricao.lower() == 'mestrado':
            self.nota_final = (self.nota_geral_publicacoes/3) + self.nota_historico
        elif self.tipo_inscricao.lower() == 'doutorado':
            self.nota_final = 0 # IMCOMPLETO

    def obter_pontuacao_publicacao1(self):
        return self.pontuacao_publicacao1

    def obter_pontuacao_publicacao2(self):
        return self.pontuacao_publicacao2

    def obter_pontuacao_publicacao3(self):
        return self.pontuacao_publicacao3

    def obter_pontuacao_publicacao4(self):
        return self.pontuacao_publicacao4

    def obter_pontuacao_publicacao5(self):
        return self.pontuacao_publicacao5

    def obter_nota_geral_publicacoes(self):
        return self.nota_geral_publicacoes 

    def obter_media_graduacao(self):
        return self.media_graduacao

    def obter_nota_historico(self):
        return self.nota_historico

    def obter_nota_final(self):
        return self.nota_final

    def print(self):
        for attr, value in self.__dict__.items():
            print(f'{attr}: {value}')

# Supondo que 'df' seja seu DataFrame
def dataframe_para_objetos(df):
    alunos = []
    for _, row in df.iterrows():
        aluno = Aluno(
            row['Nome Completo'], 
            row['Data de nascimento'], 
            row['Seu e-mail'], 
            row['Nome da mãe'], 
            row['CPF'], 
            row['Carteira de Identidade, no caso de candidatas/os de nacionalidade brasileira, ou passaporte, no caso de candidatas/os de nacionalidade estrangeira'], 
            row['Data de emissão da carteira de identidade'], 
            row['Órgão emissor da carteira de identidade e estado emissor'], 
            row['Número do título eleitoral'], 
            row['Número de série do documento militar'], 
            row['Endereço residencial'], 
            row['Cidade de residência'], 
            row['Estado de residência'], 
            row['Telefone para contato'], 
            row['Link para o currículo Lattes'], 
            row['Reservas de vagas'], 
            row['Informe o número do seu SIAPE ligado a UFPel para confirmar a candidatura às quotas de vagas para servidores da Universidade'], 
            row['Nome do Curso'], 
            row['Tipo de curso'], 
            row['Instituição'], 
            row['Ano de conclusão'], 
            row['Nome do curso'], 
            row['Tipo de curso'], 
            row['Instituição'], 
            row['Ano de conclusão'], 
            row['Local de trabalho'], 
            row['Atuação'], 
            row['Língua Inglesa (Leitura)'], 
            row['Língua Inglesa (Escrita)'], 
            row['Língua Inglesa (Fala)'], 
            row['Tipo de inscrição'], 
            row['Em que semestre faria o ingresso?'], 
            row['Orientador preferencial'], 
            row['Segunda opção'], 
            row['Terceira opção'], 
            row['Você teria dedicação integral para o curso?'], 
            row['Você manteria vínculo empregatício durante a execução do curso?'], 
            row['Você tem interesse em concorrer a uma bolsa do programa?'], 
            row['Enviar arquivo PDF contendo o Projeto de Doutorado e Memorial Acadêmico, conforme especificado no edital.'], 
            row['Título da publicação'], 
            row['Local de publicação'], 
            row['Tipo da publicação'], 
            row['Qualis do local de publicação'], 
            row['Comprovação de publicação ou aceite de publicação (PDF)'], 
            row['Primeiro autor'], 
            row['Título da publicação'], 
            row['Local de publicação'], 
            row['Tipo da publicação'], 
            row['Qualis do local de publicação'], 
            row['Comprovação de publicação ou aceite de publicação (PDF)'], 
            row['Primeiro autor'], 
            row['Título da publicação'], 
            row['Local de publicação'], 
            row['Tipo da publicação'], 
            row['Qualis do local de publicação'], 
            row['Comprovação de publicação ou aceite de publicação (PDF)'], 
            row['Primeiro autor'], 
            row['Título da publicação'], 
            row['Local de publicação'], 
            row['Tipo da publicação'], 
            row['Qualis do local de publicação'], 
            row['Comprovação de publicação ou aceite de publicação (PDF)'], 
            row['Primeiro autor'], 
            row['Título da publicação'], 
            row['Local de publicação'], 
            row['Tipo da publicação'], 
            row['Qualis do local de publicação'], 
            row['Comprovação de publicação ou aceite de publicação (PDF)'], 
            row['Primeiro autor'], 
            row['Currículo Lattes'], 
            row['Diploma de graduação OU atestado de conclusão de curso OU atestado de provável formando OU atestado de provável formando indicando que irá concluir o curso até 30 de julho de 2023 no caso de ingresso em 2023/2'], 
            row['Se aplicável, cópia do diploma de mestrado OU comprovação de cumprimento de todos requisitos para obtenção do diploma OU atestado indicando que irá concluir o seu curso de mestrado até 30 de julho de 2023 no caso de ingresso em 2023/2'], 
            row['Histórico escolar de Graduação'], 
            row['Histórico escolar de Mestrado'], 
            row['Carteira de Identidade'], 
            row['CPF, se não disponível na carteira de identidade;'], 
            row['Título de eleitor'], 
            row['Certificado de quitação com serviço militar, ou equivalente, se aplicável'], 
            row['Certidão de Casamento, no caso de mudança do nome'], 
            row['Comprovante de pagamento ou comprovante de isenção da taxa de inscrição'], 
            row['Documentação relativa a seção 6(l), 6(m), 6(n), 6(o), 6(p) ou 6(q), se aplicável'], 
            row['Outro documento se necessário de acordo com o Edital'], 
            row['ID do Usuário'], 
            row['Timestamp'], 
            row['Last Updated'], 
            row['Created By'], 
            row['Updated By'], 
            row['Draft'], 
            row['IP'], 
            row['ID'], 
            row['Key']
        )
        alunos.append(aluno)
    return alunos

# Insere a nota do histórico de graduação no objeto aluno
def inserir_historico_graduacao(alunos, historicos):
    for aluno in alunos:
        for _, row in historicos.iterrows():
            if aluno.nome_completo == row['Nome Completo']:
                aluno.media_graduacao = row['Média Histórico de Graduação']

def download_arquivo(url, diretorio_destino):
    # Extrai o ID do arquivo do link do Google Drive
    file_id = url.split('/')[-2] if '/file/d/' in url else url.split('=')[-1]
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"

    # Obtém o nome do arquivo (neste caso, você pode querer definir um nome padrão ou obter dinamicamente)
    nome_arquivo = f"{file_id}.pdf"
    caminho_completo = os.path.join(diretorio_destino, nome_arquivo)
    
    # Faz o download do arquivo
    resposta = requests.get(download_url, stream=True)
    if resposta.status_code == 200:
        with open(caminho_completo, 'wb') as arquivo:
            for chunk in resposta.iter_content(chunk_size=128):
                arquivo.write(chunk)
        print(f"Download do arquivo {nome_arquivo} concluído.")
    else:
        print(f"Erro ao baixar o arquivo {nome_arquivo}.")

def criar_pastas_alunos(alunos):
    base_dir = "Inscricoes"  # Defina o diretório base onde as pastas serão criadas
    for aluno in alunos:
        # Substitua espaços por "_" e remova caracteres especiais se necessário
        nome_pasta = aluno.nome_completo.replace(" ", "_")
        path_completo = os.path.join(base_dir, nome_pasta)
        
        # Verifica se a pasta já existe
        if not os.path.exists(path_completo):
            os.makedirs(path_completo)  # Cria a pasta
            print(f"Pasta '{nome_pasta}' criada.")
        else:
            print(f"Pasta '{nome_pasta}' já existe.")
        
        # Baixa os arquivos do aluno
        ##download_arquivo(aluno.link_curriculo_lattes, path_completo)
        #download_arquivo(aluno.arquivo_projeto_doutorado, path_completo)
        #download_arquivo(aluno.diploma_graduacao, path_completo)
        #download_arquivo(aluno.diploma_mestrado, path_completo)
        #download_arquivo(aluno.historico_graduacao, path_completo)
        #download_arquivo(aluno.historico_mestrado, path_completo)
        #download_arquivo(aluno.identidade_doc, path_completo)
        #download_arquivo(aluno.cpf_doc, path_completo)
        #download_arquivo(aluno.titulo_eleitor, path_completo)
        #download_arquivo(aluno.certificado_militar, path_completo)
        #download_arquivo(aluno.certidao_casamento, path_completo)
        #download_arquivo(aluno.comprovante_pagamento, path_completo)
        ##download_arquivo(aluno.documentacao_adicional, path_completo)
        ##download_arquivo(aluno.outro_documento, path_completo)
        #download_arquivo(aluno.comprovacao_publicacao1, path_completo)
        #download_arquivo(aluno.comprovacao_publicacao2, path_completo)
        #download_arquivo(aluno.comprovacao_publicacao3, path_completo)
        #download_arquivo(aluno.comprovacao_publicacao4, path_completo)
        #download_arquivo(aluno.comprovacao_publicacao5, path_completo)

# Cria um arquivo CSV com os alunos classificados no Mestrado
def cria_csv_classificados_mestrado(alunos):
    # Cria um DataFrame com os alunos classificados no Mestrado
    alunos_mestrado = [aluno for aluno in alunos if aluno.tipo_inscricao.lower() == 'mestrado']
    dados = {
        'Nome Completo': [aluno.nome_completo for aluno in alunos_mestrado],
        'Pontuação Publicação 1': [aluno.obter_pontuacao_publicacao1() for aluno in alunos_mestrado],
        'Pontuação Publicação 2': [aluno.obter_pontuacao_publicacao2() for aluno in alunos_mestrado],
        'Pontuação Publicação 3': [aluno.obter_pontuacao_publicacao3() for aluno in alunos_mestrado],
        'Nota Geral Publicações': [aluno.obter_nota_geral_publicacoes() for aluno in alunos_mestrado],
        'Nota Histórico Graduação': [aluno.obter_nota_historico() for aluno in alunos_mestrado],
        'Média Histórico Graduação': [aluno.obter_media_graduacao() for aluno in alunos_mestrado],
        'Nota Final': [aluno.obter_nota_final() for aluno in alunos_mestrado]
    }
    df = pd.DataFrame(dados)
    df.to_csv('classificados_mestrado.csv', index=False)
    print("Arquivo 'classificados_mestrado.csv' criado com sucesso.")         

# Função principal - controle de fluxo do programa
if __name__ == '__main__':
    
    op = 1
    
    while op == 1:
        
        # Mensagem Principal do Programa
        mensagem_principal()
        print('Digite a opção desejada:')
        escolha = int(input())
        if escolha > 5 or escolha < 1:
            print('Opção inválida!')
            escolha = int(input())
        
        # Converte csv em objetos, insere histórico de graduação, cria pastas e insere entrevistas(ainda não feito)
        if escolha == 1:
            print('Digite o nome do arquivo csv das inscricoes:')
            inscritos = le_arquivo()
            #print(inscritos)
            
            print('Digite o nome do arquivo csv do historico de Graduação:')
            historicos = le_arquivo()
            #print(historicos)
            
            alunos = dataframe_para_objetos(inscritos)
            inserir_historico_graduacao(alunos, historicos)

            criar_pastas_alunos(alunos)

        # Listagem de alunos inscritos
        elif escolha == 2:
            print("Listagem de alunos inscritos")
            for aluno in alunos:
                aluno.print()
                print("-------------------")
        
        # Classificar alunos no Mestrado
        elif escolha == 3:
            print('Classificar alunos no Mestrado')
            for aluno in alunos:
                aluno.calcular_pontuacao()
                aluno.calcula_nota_final()

            op2 = 1

            while op2 == 1:
                menu2()
                print('Digite a opção desejada:')
                escolha2 = int(input())
                if escolha2 > 3 or escolha2 < 1:
                    print('Opção inválida!')
                    escolha2 = int(input())

                # Lista alunos inscritos no Mestrado com suas pontuações
                if escolha2 == 1: 
                    for aluno in alunos:
                        print("-------------------")
                        if aluno.tipo_inscricao.lower() == 'mestrado':
                            print(f'Aluno: {aluno.nome_completo}')
                            print(f'Tipo de inscrição: {aluno.tipo_inscricao}')
                            print(f'Pontuação Publicação 1: {aluno.obter_pontuacao_publicacao1()}')
                            print(f'Pontuação Publicação 2: {aluno.obter_pontuacao_publicacao2()}')
                            print(f'Pontuação Publicação 3: {aluno.obter_pontuacao_publicacao3()}')
                            print(f'Pontuação Publicação 4: {aluno.obter_pontuacao_publicacao4()}')
                            print(f'Pontuação Publicação 5: {aluno.obter_pontuacao_publicacao5()}')
                            print(f'Nota Geral Publicações: {aluno.obter_nota_geral_publicacoes()}')
                            print(f'Média graduação: {aluno.obter_media_graduacao()}')
                            print(f'Nota histórico graduação: {aluno.obter_nota_historico()}')
                            print(f'Nota Final: {aluno.obter_nota_final()}')
                            print("-------------------")

                # Passar para csv
                elif escolha2 == 2:
                    cria_csv_classificados_mestrado(alunos)
                
                # Sair
                elif escolha2 == 3:
                    op2 = 0

        # Classificar alunos no Doutorado - INCOMPLETO
        elif escolha == 4:
            print('Classificar alunos no Doutorado')
            for aluno in alunos:
                aluno.calcular_pontuacao()
                aluno.calcula_nota_final()

            op3 = 1
            while op3 == 1:
                menu3()
                print('Digite a opção desejada:')
                escolha2 = int(input())
                if escolha2 > 3 or escolha2 < 1:
                    print('Opção inválida!')
                    escolha2 = int(input())

                if escolha2 == 1: 
                    for aluno in alunos:
                        print("-------------------")
                        if aluno.tipo_inscricao.lower() == 'doutorado':
                            print(f'Aluno: {aluno.nome_completo}')
                            print(f'Tipo de inscrição: {aluno.tipo_inscricao}')
                            print(f'Pontuação Publicação 1: {aluno.obter_pontuacao_publicacao1()}')
                            print(f'Pontuação Publicação 2: {aluno.obter_pontuacao_publicacao2()}')
                            print(f'Pontuação Publicação 3: {aluno.obter_pontuacao_publicacao3()}')
                            print(f'Pontuação Publicação 4: {aluno.obter_pontuacao_publicacao4()}')
                            print(f'Pontuação Publicação 5: {aluno.obter_pontuacao_publicacao5()}')
                            print(f'Nota Geral Publicações: {aluno.obter_nota_geral_publicacoes()}')
                            print(f'Média graduação: {aluno.obter_media_graduacao()}')
                            print(f'Nota histórico graduação: {aluno.obter_nota_historico()}')
                            print(f'Nota Final: {aluno.obter_nota_final()}')
                            print("-------------------")

                elif escolha2 == 2:
                    pass
                elif escolha2 == 3:
                    op3 = 0
            
        elif escolha == 5:
            print("Saindo do Programa...")
            op = 0