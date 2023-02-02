import subprocess

def create_file(filename):
	# crea un file
	cmd = 'touch ' + filename
	subprocess.run(cmd, shell=True)

def give_permissions(filename):
	# da' permessi completi a un file
	cmd = 'chmod 777 ' + filename
	subprocess.run(cmd, shell=True)

def check_internet_connection():
	# pinga google.com per verificare se siamo connessi a internet
	cmd = 'ping -c 2 google.com'
	subprocess.run(cmd, shell=True)
	return subprocess.run(cmd, shell=True)

def get_network_info():
	# scrive su un file apposito i dati relativi alla rete a cui siamo connessi
	create_file('network_info.txt')
	give_permissions('network_info.txt')
	cmd = 'ifconfig > network_info.txt'
	subprocess.run(cmd, shell=True)
	return subprocess.run(cmd, shell=True)

def hops_to_site(site):
	# scrive su un file apposito gli hop che vengono effettuati per connettersi
	# a google.com
	create_file('traceroute.txt')
	give_permissions('traceroute.txt')
	cmd = 'traceroute ' +  site + ' > traceroute.txt'
	subprocess.run(cmd, shell=True)
	return subprocess.run(cmd, shell=True)

def main():
	if (check_internet_connection()):
		print('I can connect to the internet! :D')
	else:
		print('I can\'t connect to the internet! :(')
	get_network_info()
	hops_to_site('google.com')

if __name__ == '__main__':
	main()
