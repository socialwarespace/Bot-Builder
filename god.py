import cor
import requests
import json

url = 'https://api.telegram.org/bot'+ cor.tok+'/'

class item:
    def __init__(**args):
        
class ReplyKeyboardMarkup(item):
        
language_keyboard = ReplyKeyboardMarkup(keyboard = [[eng], [rus]], resize_keyboard = false, one_time_keyboard = true, selective = true)

f = open("lud.txt",'r')
line = f.readline().rstrip()
print(line)
last_update_id = int(line)
f.close()

def getupdate():
    global last_update_id
    updates = requests.get(url+'getupdates').json()['result']
    for update in updates:
        if (update['update_id'] > last_update_id):
            f = open("lud.txt",'w')
            last_update_id = update['update_id']
            print(last_update_id,file=f)
            f.close()
            return update
    return None

def get_chat_id():
    global chat_id = requests.get(url+'getupdates').json()['result']['from']['id']

def send_message(chat_id,message_text):
    requests.post(url+'sendMessage?chat_id='+chat_id+'&text='message_text')

def main():
    update = getupdate() #функция возвращает самое первое обновление, которое еще не возвращала
    if (last_update_id = 1):
        get_chat_id()
        send_message(chat_id,'Язык')






while (True):
    main()
