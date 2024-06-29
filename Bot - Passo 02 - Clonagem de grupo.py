from telethon import TelegramClient, sync, events
from time import sleep
import requests
from senhas import api_hash, api_id

##+ 8562097081737

sessao = 'Repassar Mensagens' 

#def main(): funcoes de clonagem personalizadas e modificadas
def main():
    print('Monitoramento iniciado...')
    print('Clonagem de mensagens iniciado...')
    client = TelegramClient(sessao, api_id, api_hash)

    @client.on(events.NewMessage(chats=[4201129344, 1001860205395]))
    async def enviar_mensagem(event):
        if event.media:
            await client.send_file(-1002197213428, file=event.media, caption=event.raw_text)
        else:
            await client.send_message(-1002197213428, event.raw_text)

    client.start()
    client.run_until_disconnected()

main()
