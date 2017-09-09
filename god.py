import cor
import requests
import json


url = 'https://api.telegram.org/bot'+ cor.tok+'/'


class TelegramObject:
    def __init__(**args):
        pass


class ReplyKeyboardMarkup(TelegramObject):
    def __init__(self, keyboard, *resize_keyboard = false, *one_time_keyboard = false, *selective = false):
        self.json_ReplyKeyboardMarkup = json.dumps(
            'keyboard': keyboard,
            'resize_keyboard': resize_keyboard,
            'one_time_keyboard': one_time_keyboard,
            'selective': selective
            })

class KeyboardButton(TelegramObject):
    def __init__(self, text, *request_contact = false, *request_location = false):
        self.json_KeyboardButton = json.dumps(
            'text': text,
            'request_contact': request_contact,
            'request_location': request_location
            })


eng = KeyboardButton(text = 'English')
rus = KeyboardButton(text = 'Русский')
language_keyboard = ReplyKeyboardMarkup(keyboard = [[eng.json_KeyboardButton], [rus.json_KeyboardButton]], one_time_keyboard = true, selective = true)


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

def send_message(chat_id, text, *parse_mode = false, *disable_web_page_preview = false, *disable_notification = false, *reply_to_message_id = false, *reply_markup = false):
    requests.post(url+'sendMessage?chat_id='+chat_id+'&text='text'+&parse_mode='parse_mode'+&disable_web_page_preview='disable_web_page_preview'+&disable_notification='disable_notification'+&reply_to_message_id='reply_to_message_id'+&reply_markup='reply_markup')



def main():
    update = getupdate()
    if (last_update_id = 1):
        get_chat_id()
        send_message(chat_id = chat_id, text = 'Язык', reply_markup = language_keyboard.json_KeyboardButton)




while (True):
    main()
