import random

def saudacoes(nome):
    frases = [
        'Bom dia! Meu nome é Josinelson e serei o seu melhor amigo. Como você está?',
        'Olá! Tudo bem com você? Eu sou o Josinelson'
    ]
    print(frases[random.randint(0, 1)])

def recebeTexto():
    texto = 'Cliente: ' + input('Cliente: ')
    palavrasProibidas = [
        'Bocó', 'Burro', 'Estúpido', 'Idiota', 'Imbecil', 'Animal',
        'Retardado', 'Fudido', 'Fodido', 'Filho da puta', 'Arrombado',
        'Vagabundo', 'Desgraçado', 'Acéfalo', 'Corno', 'Pau no cu',
        'Filho da égua', 'Puta', 'Puto', 'Puta que pariu', 'Vai tomar no cu',
        'vtmc', 'fdp', 'vsf', 'Vai se fuder', 'Vai se foder',
        'Se mata', 'smt', 'Foda-se', 'fds', 'Foda', 'Eu te odeio', 'Morre', 'Morra', 'Maldito', 'Canalha', 'Miserável', 'Desgraça'
    ]
    
    for p in palavrasProibidas:
        if p in texto: 
            print('Não fale assim comigo!')
            return recebeTexto()
    
    return texto

def buscarResposta(nome, texto):
    with open('BaseDeDados.txt', 'a+') as conhecimento:
        conhecimento.seek(0)
        for linha in conhecimento:
            if texto.strip() == linha.strip():
                proximaLinha = conhecimento.readline()
                if 'ChatBot: ' in proximaLinha:
                    return proximaLinha.strip()
        
        if texto.replace('Cliente: ', '').strip() == 'Tchau':
            return 'fim'

        print('Desculpe, não entendi.')
        conhecimento.write('\n' + texto)
        resposta_user = input('O que você esperava que eu respondesse?\nDigite aqui: ')
        conhecimento.write('\n' + 'ChatBot: ' + resposta_user)
        return 'Entendi, obrigado pela informação.'

def exibeResposta(resposta, nome):
    if resposta == 'fim':
        print(f'{nome}: Até logo!')
        return 'fim'
    else:
        print(f'{nome}: {resposta}')
        return resposta
