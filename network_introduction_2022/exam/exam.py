import subprocess

def create_file(filename):
	# crea un file

def give_permissions(filename):
	# da' permessi completi a un file

def check_internet_connection():
	# pinga un sito per verificare se siamo connessi a internet

def get_network_info():
	# scrive su un file apposito i dati relativi alla rete a cui siamo connessi

def hops_to_site(site):
	# scrive su un file apposito gli hop che vengono effettuati per connettersi
	# a google.com

def main():
	if (check_internet_connection()):
		print('I can connect to the internet! :D')
	else:
		print('I can\'t connect to the internet! :(')

if __name__ == '__main__':
	main()
