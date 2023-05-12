def cadastrar_candidato () :
    candidato = {}
    candidato['nome'] = input("Nome do candidato: ")
    candidato['idade'] = int(input(f"Idade do candidato {candidato['nome']}: "))
    candidato['numero'] = int(input(f"Número do candidato {candidato['nome']}: "))
    candidato['partido'] = input(f"Partido do candidato {candidato['nome']}: ")
    candidato['votos'] = 0
    while True :
        candidato['cargo'] = input(f"Cargo do candidato {candidato['nome']}: ")
        if candidato['cargo'].lower() == 'presidente' or candidato['cargo'].lower() == 'governador' or candidato['cargo'].lower() == 'prefeito' :
            break
        else :
            print('Erro! Cargo inválido - presidente, governador ou prefeito\n')
    print("Candidato cadastrado com sucesso\n")
    return candidato

def cadastrar_eleitor () :
    eleitor = {}
    eleitor['nome'] = input("Nome do eleitor: ")
    eleitor['cpf'] = input(f"CPF do eleitor {eleitor['nome']}: ")
    print('Eleitor cadastrado com sucesso\n')
    return eleitor

def votar (eleitor, candidatos, cargo) :
    print('-1 para voto branco\n-2 para voto nulo')
    print(f"Votando: {eleitor}")
    status_votacao = True
    while status_votacao == True :
        voto = int(input(f"Voto para {cargo}: "))
        if voto == -1 :
            return -1
        elif voto == -2 :
            return -2
        for j in range (len(candidatos)) :
            if candidatos[j]['numero'] == voto :
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
            print("Erro! Candidato não encontrado\n")
        
def apurar_resultados (presidentes, governadores, prefeitos, votos_especiais, partidos) :
    total_votos = 0
    presidentes = sorted(presidentes, key=lambda d: d['votos'], reverse=True)
    for i in range(len(partidos)) :
        if partidos[i]['nome'] == presidentes[0]['partido'] :
            partidos[i]['eleitos'] += 1
    espacamento_nome = len(presidentes[0]['nome'])
    for i in range(len(presidentes)) :
        if len(presidentes[i]['nome']) > espacamento_nome :
            espacamento_nome = len(presidentes[i]['nome'])
    if espacamento_nome < 4 :
        espacamento_nome = 4
    espacamento_partido = len(presidentes[0]['partido'])
    for i in range(len(presidentes)) :
        if len(presidentes[i]['partido']) > espacamento_partido :
            espacamento_partido = len(presidentes[i]['partido'])
    if espacamento_partido < 7 :
        espacamento_partido = 7
    print("RANKING DO RESULTADO PARA PRESIDENTE")
    print('------------===------------')
    print('Nome', end='')
    print(' ' * (espacamento_nome - 4), end='|')
    print('Partido|Votos')
    for i in range (len(presidentes)) :
        print(f'{presidentes[i]["nome"]}', end='')
        print(' ' * (espacamento_nome - len(presidentes[i]['nome'])), end='|')
        print(f'{presidentes[i]["partido"]}', end='')
        print(' ' * (espacamento_partido - len(presidentes[i]['partido'])), end='|')
        print(f'{presidentes[i]["votos"]}')
        total_votos += presidentes[i]['votos']
    print('------------===------------')
    print(f'Total de votos: {total_votos}')
    print(f'Total de votos brancos: {votos_especiais["branco_presidente"]}')
    print(f'Total de votos nulos: {votos_especiais["nulo_presidente"]}\n')

    total_votos = 0
    governadores = sorted(governadores, key=lambda d: d['votos'], reverse=True)
    for i in range(len(partidos)) :
        if partidos[i]['nome'] == governadores[0]['partido'] :
            partidos[i]['eleitos'] += 1
    espacamento_nome = len(governadores[0]['nome'])
    for i in range(len(governadores)) :
        if len(governadores[i]['nome']) > espacamento_nome :
            espacamento_nome = len(governadores[i]['nome'])
    if espacamento_nome < 4 :
        espacamento_nome = 4
    espacamento_partido = len(governadores[0]['partido'])
    for i in range(len(governadores)) :
        if len(governadores[i]['partido']) > espacamento_partido :
            espacamento_partido = len(governadores[i]['partido'])
    if espacamento_partido < 7 :
        espacamento_partido = 7
    print("RANKING DO RESULTADO PARA GOVERNADOR")
    print('------------===------------')
    print('Nome', end='')
    print(' ' * (espacamento_nome - 4), end='|')
    print('Partido|Votos')
    for i in range (len(governadores)) :
        print(f'{governadores[i]["nome"]}', end='')
        print(' ' * (espacamento_nome - len(governadores[i]['nome'])), end='|')
        print(f'{governadores[i]["partido"]}', end='')
        print(' ' * (espacamento_partido - len(governadores[i]['partido'])), end='|')
        print(f'{governadores[i]["votos"]}')
        total_votos += governadores[i]['votos']
    print('------------===------------')
    print(f'Total de votos: {total_votos}')
    print(f'Total de votos brancos: {votos_especiais["branco_governador"]}')
    print(f'Total de votos nulos: {votos_especiais["nulo_governador"]}\n')

    total_votos = 0
    prefeitos = sorted(prefeitos, key=lambda d: d['votos'], reverse=True)
    for i in range(len(partidos)) :
        if partidos[i]['nome'] == prefeitos[0]['partido'] :
            partidos[i]['eleitos'] += 1
    espacamento_nome = len(prefeitos[0]['nome'])
    for i in range(len(prefeitos)) :
        if len(prefeitos[i]['nome']) > espacamento_nome :
            espacamento_nome = len(prefeitos[i]['nome'])
    if espacamento_nome < 4 :
        espacamento_nome = 4
    espacamento_partido = len(prefeitos[0]['partido'])
    for i in range(len(prefeitos)) :
        if len(prefeitos[i]['partido']) > espacamento_partido :
            espacamento_partido = len(prefeitos[i]['partido'])
    if espacamento_partido < 7 :
        espacamento_partido = 7
    print("RANKING DO RESULTADO PARA PREFEITO")
    print('------------===------------')
    print('Nome', end='')
    print(' ' * (espacamento_nome - 4), end='|')
    print('Partido|Votos')
    for i in range (len(prefeitos)) :
        print(f'{prefeitos[i]["nome"]}', end='')
        print(' ' * (espacamento_nome - len(prefeitos[i]['nome'])), end='|')
        print(f'{prefeitos[i]["partido"]}', end='')
        print(' ' * (espacamento_partido - len(prefeitos[i]['partido'])), end='|')
        print(f'{prefeitos[i]["votos"]}')
        total_votos += prefeitos[i]['votos']
    print('------------===------------')
    print(f'Total de votos: {total_votos}')
    print(f'Total de votos brancos: {votos_especiais["branco_prefeito"]}')
    print(f'Total de votos nulos: {votos_especiais["nulo_prefeito"]}\n')

def relatorio (eleitores, partidos) :
    eleitores = sorted(eleitores, key=lambda d: d['nome'])
    print("ELEITORES: ")
    for i in range (len(eleitores)) :
        print(eleitores[i]['nome'])
    print()
    partidos = sorted(partidos, key=lambda d: d['eleitos'], reverse=True)
    print(f"PARTIDOS COM MAIS ELEITOS: {partidos[0]['nome']} {partidos[0]['eleitos']} eleitos")
    print(f"PARTIDOS COM MENOS ELEITOS: {partidos[0]['nome']} {partidos[len(partidos) - 1]['eleitos']} eleitos\n")
    
def main () :
    print('+++++++ MENU - SIMULADOR DO SISTEMA DE VOTAÇÃO +++++++')
    presidentes = []
    governadores = []
    prefeitos = []
    eleitores = []
    partidos = []
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
            break
        elif selecao == 1 :
            cadastrando = True
            while cadastrando == True :
                partido = {}
                candidato = cadastrar_candidato()
                if candidato['cargo'].lower() == 'presidente' :
                    presidentes.append(candidato)
                elif candidato['cargo'].lower() == 'governador' :
                    governadores.append(candidato)
                else :
                    prefeitos.append(candidato)
                if len(partidos) < 1 or len(partidos) == None:
                    partido['nome'] = candidato['partido']
                    partido['eleitos'] = 0
                    partidos.append(partido)
                else :
                    for i in range(len(partidos)) :
                        if candidato['partido'] == partidos[i]['nome'] :
                            break
                    else :
                        partido['nome'] = candidato['partido']
                        partido['eleitos'] = 0
                        partidos.append(partido)
                while True :
                    nova_insercao = input("Inserir novo candidato (s/n): ")
                    if nova_insercao.lower() == 'n' :
                        cadastrando = False
                        break
                    elif nova_insercao.lower() == 's' :
                        print('Cadastrando novo candidato\n')
                        break
                    else : 
                        print('Erro! Comando inválido\n')
            print(partidos)
        elif selecao == 2 :
            while True :
                eleitores.append(cadastrar_eleitor())
                nova_insercao = input("Inserir novo eleitor (s/n): ")
                if nova_insercao.lower() == 'n' :
                    break
                elif nova_insercao.lower() == 's' :
                    print('Cadastrando novo eleitor\n')
                else : 
                    print('Erro! Comando inválido\n')
        elif selecao == 3 :
            for i in range (len(eleitores)) :
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
            apurar_resultados(presidentes, governadores, prefeitos, votos_especiais, partidos)
        elif selecao == 5 :
            relatorio(eleitores, partidos)

main()