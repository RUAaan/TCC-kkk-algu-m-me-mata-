import ChatBot as pc

nome_maquina = 'Josinelson'
pc.saudacoes(nome_maquina)

while True:
    texto = pc.recebeTexto()
    resposta = pc.buscarResposta(nome_maquina, texto)
    if pc.exibeResposta(resposta, nome_maquina) == 'fim':
        break