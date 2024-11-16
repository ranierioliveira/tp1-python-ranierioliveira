# Elaborore aqui a sua solução do TP
from collections import Counter

def exibir_menu():
  print("\n----------------------------------------")
  print("Escolha uma opção: ")
  print("1 - Adicionar item")
  print("2 - Remover amigo")
  print("3 - Verifica popularidade")
  print("4 - Exibir todos os perfis")
  print("5 - Top 5 perfis marcados como amigos")
  print("6 - Lista amigos exclusivos")
  print("12 - Encerrar escolha de opções")
  
def lista_em_dicionarios(lista):
    """ 
    Trasnforma uma lista de listas em uma lista de dicionários
    
    Parâmetros:
    list (list): lista

    Retorna:
    perfis (list): Lista de dicionários, onde cada elemento é um perfil 
    """
    perfis = []
    for elemento in lista:
        nome = elemento[0]
        idade = elemento[1]
        localizacao = (elemento[2], elemento[3])
        amigos = list(elemento[4:])
        novo_dicionario = {
            "nome": nome,
            "idade": idade, 
            "localizacao": localizacao,
            "amigos": amigos
            }
        perfis.append(novo_dicionario)
    return perfis

def valida_perfis(perfis):
    """
    Esta função filtra os perfis que não tem parâmetros obrigatórios, retirando-os
    
    Parâmetros:
    perfis (list): lista de dicionários

    Retorna:
    perfis_validadeos (list): lista de dionários nos quais tem os campos obrigatórios preenchidos
    """
    perfis_validados = []
    for perfil in perfis:
        if(perfil["nome"] and perfil["idade"] and perfil["localizacao"][0] and perfil["localizacao"][1]):
            perfis_validados.append(perfil)
    return perfis_validados

def insere_base_inicial():
    """
    Esta função adiciona perfis a partir da leitura de um arquivo txt
    """
    with open ("base_inicial.txt", "r", encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        novos_dados = []
        for linha in linhas:
            if linha != linhas[0]:
                novos_dados.append(linha.strip().split('?'))
        base_inicial_formatada = lista_em_dicionarios(novos_dados)
        perfis_validos.extend(valida_perfis(base_inicial_formatada))
        
def verifica_popularidade(nome, perfis):
    #Verifica quantas aparições um nome na lista de amigos dos usuários
    """
    Esta função retorna quantas vezes um nome está presente como amigo dos usuários da rede e dependendo do número de vezes retorna uma mensagem 
    
    Parâmetros:
    nome (str): nome a ser procurado na lista de amigos dos usuários
    perfis (list): lista dos usuários onde vai ser procurado a incidência do nome

    Retorna:
    'printa' o uma mensagem de acordo com o número de aparições, classificando como perfil popular, padrão ou iniciante.
    """
    aparicoes = 0
    for perfil in perfis:
        if nome in [amigo.lower() for amigo in perfil["amigos"]]:
            aparicoes += 1
    if aparicoes > 4:
        print(f"Perfil Popular! {nome.title()} apareceu como amigo em {aparicoes} perfis.")
    elif aparicoes > 0:
        print(f"Perfil padrão! {nome.title()} apareceu como amigo em {aparicoes} perfis.")
    else:
        print("Perfil iniciante! Sem amigos por enquanto :( .")
    
def desfazer_amizade(nome, amigo, perfis):
    """
    Esta função exclui um amigo da lista de amigos de algum usuário
    
    Parâmetros:
    nome (str): nome do usuário que terá o amigo excluído de sua lista
    amigo (str): amigo que será removido da lista de amigos
    perfis (list): lista de perfis válidos

    Retorna:
    perfis (list): lista de dionários com o amigo já excluído para o usuário em questão
    """
    for perfil in perfis:
        if nome == perfil["nome"].lower():
            if amigo in [amigo.lower() for amigo in perfil["amigos"]]:
                perfil["amigos"].remove(amigo.capitalize())
                print(f"\nAmizade com {amigo.title()} removida com sucesso!\n")
            else:
                print(f"\n{amigo.title()} não é amigo de {nome.title()}\n")
    return perfis
    
def atualiza_perfis_no_arquivo(perfis_validos):
    """
    Esta função atualiza o arquivo rede_infnet.txt, a partir da lista de perfis_validos
    
    Parâmetros:
    perfis_validos (list): lista de dicionários com os perfis atualizados 

    Retorna:
    Atualiza os usuários no arquivo 
    """
    with open("rede_infnet.txt", "w", encoding='utf-8') as arquivo_perfis:
        for perfil in perfis_validos: 
          linha = f"{perfil['nome']}: Idade {perfil['idade']}, Cidade {perfil['localizacao'][0]}, Estado {perfil['localizacao'][1]}, Amigos: {', '.join(perfil['amigos']) or 'Sem amigos cadastrados'}\n"   
          arquivo_perfis.write(linha) 
    
def top_5_amigos(perfis):
    """
    Esta função seleciona os nomes com mais aparições na lista de amigos de outros usuários
    
    Parâmetros:
    perfis (list): lista de dicionários com os perfis de todos os usuários

    Retorna:
    top_5 (dict): dicionários com o nome e o número de aparições na lista de amigos de algum perfil
    """
    contador_aparicoes = Counter()
    
    for perfil in perfis:
        for amigo in perfil["amigos"]:
            contador_aparicoes[amigo.lower()] +=1
    
    top_5 = contador_aparicoes.most_common(5)
    return top_5

def adiciona_amigo(nome, amigo, perfis):
    '''
    Esta função adiona um amigo a algum perfil
    
    Parâmetros: 
    nome (str): perfil que irá ter o amigo adicionado
    amigo (str): nome do amigo a ser adicionado
    perfis (list): lista de perfis da rede
    
    Retorna:
    perfis (list): lista de perfis com um dos usuários com o amigo adicionado
    '''
    for perfil in perfis:
        if nome  == perfil["nome"].lower():
            perfil["amigos"].append(amigo)
            print(f"\n{amigo} adicionado a lista de amigos de {nome.capitalize()} com sucesso!\n")
    return perfis

def identifica_amigos_exclusivos(perfis):
    '''
    Esta função identifica os amigos exclusivos de cada usuário
    
    Parâmetro:
    perfis (list): lista de perfis da rede
    
    Retorna:
    'Printa' aqueles itens que tem amigos exclusivos
    '''   
    amigos_exclusivos = {}
    
    for perfil_atual in perfis:
        amigos_comuns = set()
        
        #vai iterar novamente e selecionar os que são diferente ao que está sendo analisado
        for outro_perfil in perfis:
            if outro_perfil != perfil_atual:
                #transforma os amigos atuais em um set e adiona os comuns no set criado anteriormente
                amigos_comuns.update(set(perfil_atual["amigos"]).intersection(outro_perfil["amigos"]))
        
        exclusivos = set(perfil_atual["amigos"]) - amigos_comuns
        #adicionando ao dicionário
        amigos_exclusivos[perfil_atual["nome"]] = list(exclusivos)
        
    for nome, exclusivos in amigos_exclusivos.items():
        if exclusivos:
            print(f"{nome} tem os seguintes amigos exclusivos: {', '.join(exclusivos) if exclusivos else 'Nenhum amigo exclusivo encontrado'}")
    
usuarios = [
    ['Ranieri', 22, 'Campinas', 'SP'],
    ['Maria', 20, 'Jaguaríuna', 'SP'],
    ['João', 32, 'Hortolândia', 'SP'],
    ['Geovana', 21, 'Sumaré', 'SP'],
    ['Jorge', 28, 'Valinhos', 'SP'],
    ['Luana', 19, 'Holambra', ''],
    ['José', 25, '', 'MG']
]

perfis = lista_em_dicionarios(usuarios)
perfis_validos = valida_perfis(perfis)
insere_base_inicial()
perfis_validos[1]["amigos"].append("Lizandra")#Adicionando um amigo a um usuário
atualiza_perfis_no_arquivo(perfis_validos)



while True:
   exibir_menu()
   opcao = input("\nDigite o número da opção escolhida: ").lower().strip()
   if opcao == "1":
    perfil_pessoal = input("Digite o nome cadastrado no seu perfil: ").lower().strip()
    amigo_a_ser_adicionado = input("Digite o nome do amigo a ser adicionado: ").capitalize().strip()
    perfis_validos = adiciona_amigo(perfil_pessoal, amigo_a_ser_adicionado, perfis_validos)
    atualiza_perfis_no_arquivo(perfis_validos)
    

   elif opcao == "2":
    perfil_pessoal = input("Digite o nome cadastrado no seu perfil: ").lower().strip()
    amigo_a_ser_excluido = input("Digite o nome do amigo a ser removido: ").lower().strip()
    perfis_validos = desfazer_amizade(perfil_pessoal, amigo_a_ser_excluido, perfis_validos)
    atualiza_perfis_no_arquivo(perfis_validos)
    
   elif opcao == "3":
    perfil_popular = input("Digite um nome para verificar se ele é popular: ").strip().lower()
    verifica_popularidade(perfil_popular, perfis_validos)
    
   elif opcao == "4":
    for perfil in perfis_validos:
        print(perfil["nome"])
    
   elif opcao == "5":
    top_5 = top_5_amigos(perfis_validos)
    for amigo, quantidade in top_5:
        print(f"{amigo.title()} com {quantidade} amigo(s)")
        
   elif opcao == "6":
        identifica_amigos_exclusivos(perfis_validos)
   
   elif opcao == "12":
    print("\nMenu encerrado!")
    break
   else:
       
    print("\nEscolha errada, tente novamente!\n")
 
'''
lista, dicionários, tupla
Listas são agrupamentos de dados, nos quais, geralmente possuem algo em comum

Dicionários são iteráveis, porém diferentes das listas têm uma chave para acessar determinada informação.

Tuplas seguem quase a mesma lógica das listas, porém sua particularidade é que são imutáveis
'''