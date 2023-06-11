def cadastrar_candidato () :
    # Cadastra um candidato criando um dicionário candidato {nome, idade, numero, partido e votos}
    candidato = {}
    candidato['nome'] = input("Nome do candidato: ")
    candidato['idade'] = int(input(f"Idade do candidato {candidato['nome']}: "))
    candidato['numero'] = int(input(f"Número do candidato {candidato['nome']}: "))
    candidato['partido'] = input(f"Partido do candidato {candidato['nome']}: ")
    candidato['votos'] = 0
    while True :
        # Permite apenas cadastrar um candidato com o cargo de presidente, governador ou prefeito
        candidato['cargo'] = input(f"Cargo do candidato {candidato['nome']}: ")
        if candidato['cargo'].lower() == 'presidente' or candidato['cargo'].lower() == 'governador' or candidato['cargo'].lower() == 'prefeito' :
            break
        else :
            print('Erro! Cargo inválido - presidente, governador ou prefeito\n')
    print("Candidato cadastrado com sucesso\n")
    return candidato

def cadastrar_eleitor () :
    # Cadastra um eleitor criando um dicionário eleitore {nome e cpf}
    eleitor = {}
    eleitor['nome'] = input("Nome do eleitor: ")
    eleitor['cpf'] = input(f"CPF do eleitor {eleitor['nome']}: ")
    print('Eleitor cadastrado com sucesso\n')
    return eleitor

def votar (eleitor, candidatos, cargo) :
    # Faz o processo de votação
    print('-1 para voto branco\n-2 para voto nulo')
    print(f"Votando: {eleitor}")
    status_votacao = True
    while status_votacao == True :
        voto = int(input(f"Voto para {cargo}: "))
        # Caso o voto for -1 ou -2, retorna esse valor e encerra a votação para esse eleitor
        if voto == -1 :
            while True :
                confirmar_voto = input("Deseja votar em branco (s/n): ")
                if confirmar_voto.lower() == 's' :
                    return -1
                elif confirmar_voto.lower() == 'n' :
                    break
                else :
                    print('Erro! Comando inválido\n')
        elif voto == -2 :
            while True :
                confirmar_voto = input("Deseja votar nulo (s/n): ")
                if confirmar_voto.lower() == 's' :
                    return -2
                elif confirmar_voto.lower() == 'n' :
                    break
                else :
                    print('Erro! Comando inválido\n')
        for j in range (len(candidatos)) :
            # Itera sobre a lista candidatos
            if candidatos[j]['numero'] == voto :
                # Caso haja uma correspondecia do número de um candidato com o número do voto fornecido, pede confirmação de voto
                confirmar_voto = input(f"Deseja votar no(a) {candidatos[j]['nome']} do partido {candidatos[j]['partido']} (s/n): ")
                if confirmar_voto.lower() == 'n' :
                    break
                elif confirmar_voto.lower() == 's' :
                    candidatos[j]['votos'] += 1
                    print("Voto confirmado!\n")
                    return 0
                else : 
                    print('Erro! Comando inválido\n')
        else :
            # Caso depois da iteração, não seja encontrado nenhum candidato com o número do voto fornecido, exibe um erro
            print("Erro! Candidato não encontrado\n")
        
def apurar_resultados (presidentes, governadores, prefeitos, votos_especiais, partidos) :   
    texto = [] # Inicializa uma lista que será usada para a gravação da apuração
    total_votos = 0
    presidentes = sorted(presidentes, key=lambda d: d['votos'], reverse=True) # Ordena a lista presidentes por ordem de voto
    for i in range(len(partidos)) :
        # Define o partido que ganhou a eleição para presidente
        if partidos[i]['nome'] == presidentes[0]['partido'] :
            partidos[i]['eleitos'] += 1
    # Faz o espaçamento necessário para a tabulação dos nome dos candidatos
    espacamento_nome = len(presidentes[0]['nome'])
    for i in range(len(presidentes)) :
        if len(presidentes[i]['nome']) > espacamento_nome :
            espacamento_nome = len(presidentes[i]['nome'])
    if espacamento_nome < 4 :
        espacamento_nome = 4
    # Faz o espaçamento necessário para a tabulação dos nome dos partidos
    espacamento_partido = len(presidentes[0]['partido'])
    for i in range(len(presidentes)) :
        if len(presidentes[i]['partido']) > espacamento_partido :
            espacamento_partido = len(presidentes[i]['partido'])
    if espacamento_partido < 7 :
        espacamento_partido = 7
    # Printa o cabeçalho da tabela
    print("RANKING DO RESULTADO PARA PRESIDENTE")
    print('------------===------------')
    print('Nome', end='')
    print(' ' * (espacamento_nome - 4), end='|')
    print('Partido|Votos')
    # Salva o cabeçalho na lista de gravação
    texto.append("RANKING DO RESULTADO PARA PRESIDENTE")
    texto.append('------------===------------')
    texto.append('Nome' + ' ' * (espacamento_nome - 4) + "|"+ 'Partido|Votos')

    for i in range (len(presidentes)) :
        # Faz a tabulação dos dados dos candidatos
        print(f'{presidentes[i]["nome"]}', end='')
        print(' ' * (espacamento_nome - len(presidentes[i]['nome'])), end='|')
        print(f'{presidentes[i]["partido"]}', end='')
        print(' ' * (espacamento_partido - len(presidentes[i]['partido'])), end='|')
        print(f'{presidentes[i]["votos"]}')
        # Salva os dados do candidato na lista de gravação
        texto.append(f'{presidentes[i]["nome"]}' + ' ' * (espacamento_nome - len(presidentes[i]['nome'])) + f'|{presidentes[i]["partido"]}' + ' ' * (espacamento_partido - len(presidentes[i]['partido'])) + f'|{presidentes[i]["votos"]}')
        total_votos += presidentes[i]['votos']
    print('------------===------------')
    # Exibe as informações de total de votos, nulos e brancos
    print(f'Total de votos: {total_votos}')
    print(f'Total de votos brancos: {votos_especiais["branco_presidente"]}')
    print(f'Total de votos nulos: {votos_especiais["nulo_presidente"]}\n')
    # Salva as informações de total de votos, nulos e brancos na lista de gravação
    texto.append('------------===------------')
    texto.append(f'Total de votos: {total_votos}')
    texto.append(f'Total de votos brancos: {votos_especiais["branco_presidente"]}')
    texto.append(f'Total de votos nulos: {votos_especiais["nulo_presidente"]}\n')
    texto.append('')

    total_votos = 0
    governadores = sorted(governadores, key=lambda d: d['votos'], reverse=True) # Ordena a lista governadores por ordem de voto
    for i in range(len(partidos)) :
        # Define o partido que ganhou a eleição para governador
        if partidos[i]['nome'] == governadores[0]['partido'] :
            partidos[i]['eleitos'] += 1
    # Faz o espaçamento necessário para a tabulação dos nome dos candidatos
    espacamento_nome = len(governadores[0]['nome'])
    for i in range(len(governadores)) :
        if len(governadores[i]['nome']) > espacamento_nome :
            espacamento_nome = len(governadores[i]['nome'])
    if espacamento_nome < 4 :
        espacamento_nome = 4
    # Faz o espaçamento necessário para a tabulação dos nome dos partidos
    espacamento_partido = len(governadores[0]['partido'])
    for i in range(len(governadores)) :
        if len(governadores[i]['partido']) > espacamento_partido :
            espacamento_partido = len(governadores[i]['partido'])
    if espacamento_partido < 7 :
        espacamento_partido = 7
    # Printa o cabeçalho da tabela
    print("RANKING DO RESULTADO PARA GOVERNADOR")
    print('------------===------------')
    print('Nome', end='')
    print(' ' * (espacamento_nome - 4), end='|')
    print('Partido|Votos')
    # Salva o cabeçalho na lista de gravação
    texto.append("RANKING DO RESULTADO PARA GOVERNADOR")
    texto.append('------------===------------')
    texto.append('Nome' + ' ' * (espacamento_nome - 4) + "|"+ 'Partido|Votos')
    for i in range (len(governadores)) :
        # Faz a tabulação dos dados dos candidatos
        print(f'{governadores[i]["nome"]}', end='')
        print(' ' * (espacamento_nome - len(governadores[i]['nome'])), end='|')
        print(f'{governadores[i]["partido"]}', end='')
        print(' ' * (espacamento_partido - len(governadores[i]['partido'])), end='|')
        print(f'{governadores[i]["votos"]}')
        # Salva os dados do candidato na lista de gravação
        texto.append(f'{governadores[i]["nome"]}' + ' ' * (espacamento_nome - len(governadores[i]['nome'])) + f'|{governadores[i]["partido"]}' + ' ' * (espacamento_partido - len(governadores[i]['partido'])) + f'|{governadores[i]["votos"]}')
        total_votos += governadores[i]['votos']
    print('------------===------------')
    # Exibe as informações de total de votos, nulos e brancos
    print(f'Total de votos: {total_votos}')
    print(f'Total de votos brancos: {votos_especiais["branco_governador"]}')
    print(f'Total de votos nulos: {votos_especiais["nulo_governador"]}\n')
    # Salva as informações de total de votos, nulos e brancos na lista de gravação
    texto.append('------------===------------')
    texto.append(f'Total de votos: {total_votos}')
    texto.append(f'Total de votos brancos: {votos_especiais["branco_governador"]}')
    texto.append(f'Total de votos nulos: {votos_especiais["nulo_governador"]}\n')
    texto.append('')

    total_votos = 0
    prefeitos = sorted(prefeitos, key=lambda d: d['votos'], reverse=True) # Ordena a lista prefeitos por ordem de voto
    for i in range(len(partidos)) :
        # Define o partido que ganhou a eleição para prefeito
        if partidos[i]['nome'] == prefeitos[0]['partido'] :
            partidos[i]['eleitos'] += 1
    # Faz o espaçamento necessário para a tabulação dos nomes dos candidatos
    espacamento_nome = len(prefeitos[0]['nome'])
    for i in range(len(prefeitos)) :
        if len(prefeitos[i]['nome']) > espacamento_nome :
            espacamento_nome = len(prefeitos[i]['nome'])
    if espacamento_nome < 4 :
        espacamento_nome = 4
    # Faz o espaçamento necessário para a tabulação dos nome dos partidos
    espacamento_partido = len(prefeitos[0]['partido'])
    for i in range(len(prefeitos)) :
        if len(prefeitos[i]['partido']) > espacamento_partido :
            espacamento_partido = len(prefeitos[i]['partido'])
    if espacamento_partido < 7 :
        espacamento_partido = 7
    # Printa o cabeçalho da tabela
    print("RANKING DO RESULTADO PARA PREFEITO")
    print('------------===------------')
    print('Nome', end='')
    print(' ' * (espacamento_nome - 4), end='|')
    print('Partido|Votos')
    # Salva a o cabeçalho na lista de gravação
    texto.append("RANKING DO RESULTADO PARA PREFEITO")
    texto.append('------------===------------')
    texto.append('Nome' + ' ' * (espacamento_nome - 4) + "|"+ 'Partido|Votos')
    for i in range (len(prefeitos)) :
        # Faz a tabulação dos dados dos candidatos
        print(f'{prefeitos[i]["nome"]}', end='')
        print(' ' * (espacamento_nome - len(prefeitos[i]['nome'])), end='|')
        print(f'{prefeitos[i]["partido"]}', end='')
        print(' ' * (espacamento_partido - len(prefeitos[i]['partido'])), end='|')
        print(f'{prefeitos[i]["votos"]}')
        # Salva os dados do candidato na lista de gravação
        texto.append(f'{prefeitos[i]["nome"]}' + ' ' * (espacamento_nome - len(prefeitos[i]['nome'])) + f'|{prefeitos[i]["partido"]}' + ' ' * (espacamento_partido - len(prefeitos[i]['partido'])) + f'|{prefeitos[i]["votos"]}')
        total_votos += prefeitos[i]['votos']
    print('------------===------------')
    # Exibe as informações de total de votos, nulos e brancos
    print(f'Total de votos: {total_votos}')
    print(f'Total de votos brancos: {votos_especiais["branco_prefeito"]}')
    print(f'Total de votos nulos: {votos_especiais["nulo_prefeito"]}\n')
    # Salva as informações de total de votos, nulos e brancos na lista de gravação
    texto.append('------------===------------')
    texto.append(f'Total de votos: {total_votos}')
    texto.append(f'Total de votos brancos: {votos_especiais["branco_prefeito"]}')
    texto.append(f'Total de votos nulos: {votos_especiais["nulo_prefeito"]}\n')
    texto.append('')
    
    return texto # Retorna a lista de gravação

def relatorio (eleitores, partidos) :
    # Ordena os eleitores por ordem alfabética
    eleitores = sorted(eleitores, key=lambda d: d['nome'])
    # Printa os eleitores e seus respectivos CPF
    print("ELEITORES: ")
    for i in range (len(eleitores)) :
        print(f'{eleitores[i]["nome"]} - CPF: {eleitores[i]["cpf"]}')
    print()
    # Printa os partidos com mais eleitos e com menos eleitos
    partidos = sorted(partidos, key=lambda d: d['eleitos'], reverse=True)
    print(f"PARTIDOS COM MAIS ELEITOS: {partidos[0]['nome']} {partidos[0]['eleitos']} eleitos")
    print(f"PARTIDOS COM MENOS ELEITOS: {partidos[len(partidos) - 1]['nome']} {partidos[len(partidos) - 1]['eleitos']} eleitos\n")

def gravar_apuracao (texto) :
    if len(texto) == 0 :
        print("Erro! Não foi feita eleição")
        return
    # Faz a gravação da apuração em um arquivo .txt chamado apuracao
    file = open('apuracao.txt', 'w')
    for i in range (len(texto)) :
        file.write(texto[i] + "\n")
    file.close()
    print('Gravação em txt feita com sucesso\n')

def main () :
    print('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++')
    # Inicializa todas as listas que serão usadas
    presidentes = []
    governadores = []
    prefeitos = []
    eleitores = []
    partidos = []
    apurado = False
    votos_especiais = {
        'nulo_presidente': 0,
        'branco_presidente':0,
        'nulo_governador': 0,
        'branco_governador':0,
        'nulo_prefeito': 0,
        'branco_prefeito':0,
    }

    while True :
        print('1. Cadastrar Candidatos\n2. Cadastrar Eleitores\n3. Votar\n4. Apurar Resultados\n5. Relatório e Estatísticas\n6. Gravar Apuração\n7. Encerrar')
        selecao = int(input("Opção escolhida: "))
        print()
        if selecao == 7 :
            # Caso for selecionado 7, o programa encerra
            break
        elif selecao == 1 :
            # Caso for selecionado 1, começa o cadastramento de candidatos
            cadastrando = True
            while cadastrando == True :
                partido = {}
                # Cadastra o candidato na respectiva lista de seu cargo
                candidato = cadastrar_candidato()
                if candidato['cargo'].lower() == 'presidente' :
                    presidentes.append(candidato)
                elif candidato['cargo'].lower() == 'governador' :
                    governadores.append(candidato)
                else :
                    prefeitos.append(candidato)
                # Popula a lista partidos 
                if len(partidos) < 1 :
                    # Se a lista partido estiver vazia, apenas adiciona o partido do candidato
                    partido['nome'] = candidato['partido']
                    partido['eleitos'] = 0
                    partidos.append(partido)
                else :
                    # Se a lista possuir partidos, confirmar se o partido do candidato já existe
                    for i in range(len(partidos)) :
                        if candidato['partido'] == partidos[i]['nome'] :
                            break
                    else :
                        partido['nome'] = candidato['partido']
                        partido['eleitos'] = 0
                        partidos.append(partido)
                while True :
                    # Pergunta se fará um novo cadastro
                    nova_insercao = input("Inserir novo candidato (s/n): ")
                    if nova_insercao.lower() == 'n' :
                        cadastrando = False
                        break
                    elif nova_insercao.lower() == 's' :
                        print('Cadastrando novo candidato\n')
                        break
                    else : 
                        print('Erro! Comando inválido\n')
        elif selecao == 2 :
            # Caso for selecionado 2, começa o cadastramento de eleitores
            while True :
                # Adiciona o eleitor na lista de eleitores
                eleitores.append(cadastrar_eleitor())
                nova_insercao = input("Inserir novo eleitor (s/n): ")
                # Pergunta se fará um novo cadastro
                if nova_insercao.lower() == 'n' :
                    break
                elif nova_insercao.lower() == 's' :
                    print('Cadastrando novo eleitor\n')
                else : 
                    print('Erro! Comando inválido\n')
        elif selecao == 3 :
            # Caso for selecionado 3, começa o processo de votação
            if len(presidentes) == 0 or len(governadores) == 0 or len(prefeitos) == 0 :
                print('Erro! 1 candidato para cada cargo é necessário\n')
            else :
                for i in range (len(eleitores)) :
                    # Para cada eleitor, serão feitos 3 votos, prefeito, governador e presidente
                    # Caso o processo de votação retornar -1, aumenta os votos em branco daquela respectiva categoria de votação
                    # Caso o processo de votação retornar -2, aumenta os votos nulo daquela respectiva categoria de votação
                    votacao = votar(eleitores[i]['nome'], prefeitos, "prefeito")
                    if votacao == -1 :
                        votos_especiais['branco_prefeito'] += 1
                    elif votacao == -2 :
                        votos_especiais['nulo_prefeito'] += 1
                    votacao = votar(eleitores[i]['nome'], governadores, "governador")
                    if votacao == -1 :
                        votos_especiais['branco_governador'] += 1
                    elif votacao == -2 :
                        votos_especiais['nulo_governador'] += 1
                    votacao = votar(eleitores[i]['nome'], presidentes, "presidente")
                    if votacao == -1 :
                        votos_especiais['branco_presidente'] += 1
                    elif votacao == -2 :
                        votos_especiais['nulo_presidente'] += 1
        elif selecao == 4 :
            # Caso for selecionado 4, começa o processo de apuração eleitoral
            if len(presidentes) == 0 or len(governadores) == 0 or len(prefeitos) == 0 :
                print('Erro! 1 candidato para cada cargo é necessário\n')
            else :
                texto = apurar_resultados(presidentes, governadores, prefeitos, votos_especiais, partidos)
                apurado = True
        elif selecao == 5 :
            # Caso for selecionado 5, exibe um relatório da eleição
            if len(eleitores) == 0 or len(partidos) == 0 :
                print("Erro! Partido ou eleitores sem conteúdo")
            else :
                relatorio(eleitores, partidos)
        elif selecao == 6 :
            # Caso for selecionado 6, grava a apuração em um arquivo .txt            
            if apurado == True :
                gravar_apuracao(texto)
            else :
                print('Erro! Apuração não foi feita\n')
main()