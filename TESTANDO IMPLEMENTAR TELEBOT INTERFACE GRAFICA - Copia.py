import asyncio
import threading
import re
import PySimpleGUI as sg
import threading
from telethon import TelegramClient, sync, events, types
from time import sleep
import requests
#from senhas import api_hash, api_id

#variaveis de sessao
sessao = 'Repassar Mensagens'
api_id = 21060671
api_hash = '82847248179d545b34db35f11e4044fd'
##sessao = '##+ 8562097081737'


# Crie a janela com um botão para iniciar o monitoramento
layout = [
    [sg.Text("Monitoramento do POKET GAMES MIX by DENVER PICOROSO")],
    [sg.Button("Iniciar Monitoramento")]
]

window = sg.Window("Monitoramento de Mensagens", layout)

# METODO SUB
def substituir_links_por_palavras(texto):
    # PADRAO QUE DETECTA OS LINKS NO AUTOMATICO (http ou https) (IA)
    padrao = r'https?://\S+'

    # SUBSTITUINDO TODOS OS LINKS PELO MEU LINK PRINCIPAL DE COMISSAO
    novo_texto = re.sub(padrao, 'bit.ly/SuperBotDuarteGames', texto)

    # SUBSTITUINDO MAIS ITENS, CONFORME FOR NECESSARIO
    
    novo_texto = novo_texto.replace('✅ 𝔽𝔸𝕃ℍ𝔸 𝔻𝔼𝕋𝔼ℂ𝕋𝔸𝔻𝔸!!', '✅ NOVA BRECℍ𝔸 𝔻𝔼𝕋𝔼ℂ𝕋𝔸𝔻𝔸!!')
    novo_texto = novo_texto.replace('🚥 Aguarde Novas Hackes ☠', '🚥 Aguarde por novas Brechas ☠...')
    novo_texto = novo_texto.replace('🚨 𝙎𝙞𝙣𝙖𝙡 𝙖𝙥𝙚𝙣𝙖𝙨 𝙥𝙖𝙧𝙖 𝙖 𝙥𝙡𝙖𝙩𝙖𝙛𝙤𝙧𝙢𝙖 𝙖𝙗𝙖𝙞𝙭𝙤! 👇', '🚨👇👇𝙎𝙞𝙣𝙖𝙡 𝙥𝙖𝙧𝙖 𝙖 𝙥𝙡𝙖𝙩𝙖𝙛𝙤𝙧𝙢𝙖 𝙖𝙗𝙖𝙞𝙭𝙤!')

    return novo_texto

def monitorar_mensagens():
    # Crie um novo loop de eventos para esta thread
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # Seu código de monitoramento de mensagens aqui
    # Certifique-se de incluir a lógica do seu evento "enviar_mensagem"
    # Exemplo:
    # async def enviar_mensagem(event):
    #     ...

    def main():
        print('Monitoramento do Grupo "POKET GAMES MIX" iniciado...')
        print('Clonando mensagens para o Grupo "VIP do Tigrinho - DUARTE YHGAMES" iniciado...')
        print('Processando...')
        client = TelegramClient(sessao, api_id, api_hash)

    # ABAIXO, VARIAVEIS SOMENTE PARA OS "GRUPOS RECEPTORES"

        receptor01 = -1002179776070                                             # grupo receptor 01 "tigrinho YHGames"
        monitorado01 = -1002191614321                                           # grupo para testes
        bacbo = -1001860205395                                                  # grupo bacbo vip
        grupotigre77k = -1002041574468                                          # grupo tigrinho 77k membros para capturar sinais
        canalbitcardsvip = -1001904165641                                       # canal bit cards vip p capturar sinais football studios cards
        canalreceptormonitorbitcards = -1002155651037                           # canal receptor monitor bit cards, para portavos e conferencia
        canalpocketgamesmix = -1002245571308                                    # canal de slots sinais pocket games  
        

    # ABAIXO TEM OS GRUPOS DAONDE SERAO MONITORADO E RETIRADAS AS MENSAGENS:
        
        @client.on(events.NewMessage(chats=[1002191614321, 1002245571308]))

    # ABAIXO, VARIAVEIS SOMENTE PARA O "@client.on events"
        
        #receptor01 = 1002179776070     #grupo receptor 01 "tigrinho YHGames"
        #amonitorado01 = 1002191614321   #grupo para testes onde posto conteudo para trabsnitir
        #abacbo = 1001860205395            #grupo do bac bo com sinais
        #agrupotigre77k = 1002041574468    #grupo tigrinho com 77k e sinais para transmitir

    # MONITORANDO AS MENSAGENS:

        async def enviar_mensagem(event):
            if event.media:

        # SUBSTITUINDO OS LINKS POR TERMOS PERSONALIZADOS  E ENVIANDO PARA OS GRUPOS DE DESTINO

                nova_caption = substituir_links_por_palavras(event.raw_text.replace('STARTBET','YHGAMES'))
                await client.send_file(receptor01, file=event.media, caption=nova_caption)
            else:
                nova_mensagem = substituir_links_por_palavras(event.raw_text.replace('STARTBET','YHGAMES'))
                await client.send_message(receptor01, nova_mensagem)

        # VERIFICANDO SE A MENSAGEM TEM ALGUMA WEBPAGE

                if isinstance(event.media, types.MessageMediaWebPage):

        # EXTRAIR A URL DA WEBPAGE LOCALIZADA, SE HOUVER ALGUMA

                    url = event.media.webpage.url
                    await client.send_message(receptor01, f"Confira esta página: {url}")


                
                
    # SUBSTITUINDO TODOS OS LINKS E NOMES DE OUTRAS PLATAFORMAS PELO NOME DE INTERESSE (METODO ANTIGO)

                #await client.send_file(receptor01, file=event.media, caption=event.raw_text.replace('Playcassino','https://bit.ly/SuperBotDuarteGames '))
            #else:
                #await client.send_message(receptor01, event.raw_text.replace('Playcassino','https://bit.ly/SuperBotDuarteGames'))

                #await client.send_message(receptor01, event.raw_text.replace('Registre-se Aqui','https://bit.ly/SuperBotDuarteGames '))

                #await client.send_message(receptor01, event.raw_text.replace('Acelerabet - Bac Bo!','https://bit.ly/SuperBotDuarteGames '))

        client.start()
        client.run_until_disconnected()

    if __name__ == '__main__':   # (IA)
        main()

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Iniciar Monitoramento":
        # Inicie o monitoramento em uma thread separada
        t = threading.Thread(target=monitorar_mensagens)
        t.start()

window.close()



















