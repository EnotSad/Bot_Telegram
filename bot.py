import requests
import json
import misc
from nbrb import get_usd
from nbrb import get_eur
from time import sleep

token = misc.token

#https://api.telegram.org/bot744518437:AAE1aIixkXkLbnpVcV51E_sIQwUnyNkC7ZM/sendMessage?chat_id=461454793&text=hi
chislo = 0
URL = 'https://api.telegram.org/bot' + token + '/'
global last_update_id
last_update_id = 0


def get_updates():
	url = URL + 'getupdates'
	print(url)
	r = requests.get(url)
	return r.json()



def get_message():
	data = get_updates()
	last_objet = data['result'][-1]
	current_update_id = last_objet['update_id']
	
	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id

		chat_id = data['result'][-1]['message']['chat']['id']
		message_text = data['result'][-1]['message']['text']

		message = {'chat_id': chat_id,
					'text': message_text}

		return message
	return None


def send_message(chat_id, text='Wait a second, please....'):
	
	url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id,text)
	requests.get(url)




def main():

	while True:
			
		answer = get_message()
		if answer != None:

		
			
			
			chat_id = answer['chat_id']
			text = answer['text']

			if text == '/start':
				send_message(chat_id,'Приветствую! Я Enot_Bot, и я помогу тебе с курсами валют.')

			if text == 'usd':
				send_message(chat_id,get_usd())
			if text == '$':
				send_message(chat_id,get_usd())
			if text ==  'доллар':
				send_message(chat_id,get_usd())
			if text == 'eur':
				send_message(chat_id,get_eur())
			if text == 'евро':
				send_message(chat_id,get_eur())
		else:
			continue 

		sleep(2)




	#d = get_updates()
#	with open('updates.json', 'w') as file:
#		json.dump(d,file, indent=2, ensure_ascii=False)
	





if __name__ == '__main__':
	main()