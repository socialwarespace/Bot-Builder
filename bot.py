import con
import requests
import json

url = 'https://api.telegram.org/bot'+ con.tok+'/'

f = open("lud.txt",'r')
line = f.readline().rstrip()
print(line)
last_update_id = int(line)
f.close()

#def send_message(chat_id, text):
#def dosmthwithupd(message):

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
    
        






while (True):
    main()
