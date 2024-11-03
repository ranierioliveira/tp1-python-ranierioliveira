# Elaborore aqui a sua solução do TP
def lista_em_dicionarios(lista):
    #pega uma lista e transforma em um dicionário
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
    #valida se não há campos vazios 
    perfis_validados = []
    for perfil in perfis:
        if(perfil["nome"] and perfil["idade"] and perfil["localizacao"][0] and perfil["localizacao"][1]):
            perfis_validados.append(perfil)
    return perfis_validados

def insere_base_inicial():
    #le a base inicial insere perfis válidos
    with open ("base_inicial.txt", "r", encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        novos_dados = []
        for linha in linhas:
            novos_dados.append(linha.strip().split('?'))
        base_inicial_formatada = lista_em_dicionarios(novos_dados)
        perfis_validos.extend(valida_perfis(base_inicial_formatada))
        
        
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
perfis_validos[1]["amigos"].append("Lizandra")
print(perfis_validos[1]["amigos"]) #Adicionando um amigo a um usuário
# for perfil in perfis_validos:
#     print(perfil)
    
with open("rede_infnet.txt", "w", encoding='utf-8') as arquivo_perfis:
    for perfil in perfis_validos:
          linha = f"{perfil['nome']}: Idade {perfil['idade']}, Cidade {perfil['localizacao'][0]}, Estado {perfil['localizacao'][1]}, Amigos: {', '.join(perfil['amigos']) or 'Sem amigos cadastrados'}\n"   
          arquivo_perfis.write(linha) 
    

    
#perfis_validos.items() vai retornar algo como "Ranieri": [22, "Campinas", "SP"]      
        
'''
lista, dicionários, tupla
Listas são agrupamentos de dados, nos quais, geralmente possuem algo em comum

Dicionários são iteráveis, porém diferentes das listas têm uma chave para acessar determinada informação.

Tuplas seguem quase a mesma lógica das listas, porém sua particularidade é que são imutáveis
'''