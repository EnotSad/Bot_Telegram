import requests




def get_usd():
	url = 'http://free.currencyconverterapi.com/api/v5/convert?q=USD_BYN&compact=y'
	response = requests.get(url).json()
	price=response["USD_BYN"]['val']
	return str(price) + ' USD_BYN'
def get_eur():
	url = 'http://free.currencyconverterapi.com/api/v5/convert?q=EUR_BYN&compact=y'
	response = requests.get(url).json()
	price=response["EUR_BYN"]['val']
	return str(price) + ' EUR_BYN'